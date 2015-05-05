using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;
using System.IO;
using System.Windows.Forms;
using ESRI.ArcGIS.ArcMapUI;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.DataSourcesGDB;
using ESRI.ArcGIS.Geometry;
using ESRI.ArcGIS.Display;
using Point = ESRI.ArcGIS.Geometry.Point;

namespace HistogramClassification
{
    public class HistoClass : ESRI.ArcGIS.Desktop.AddIns.Button
    {
        public HistoClass()
        {
        }

        protected override void OnClick()
        {
            //
            //  TODO: Sample code showing how to access button host
            //
            ArcMap.Application.CurrentTool = null;

            //Create the workspace and then create the feature class.
            Type factoryType = Type.GetTypeFromProgID("esriDataSourcesGDB.FileGDBWorkspaceFactory");
            IWorkspaceFactory workspaceFactory = Activator.CreateInstance(factoryType) as IWorkspaceFactory;
            IWorkspace workspace = workspaceFactory.OpenFromFile(System.IO.Path.Combine(System.IO.Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location), @"Data\testData.gdb").ToString(), 0);
            IFeatureWorkspace featureWorkspace = workspace as IFeatureWorkspace;

            IFeatureClass createdFeatureClass = CreateFeatureClass("Reddies", featureWorkspace);

            //Generate data for the feature class
            BoboDataGeneration(createdFeatureClass, featureWorkspace);

            //Create the layer and add it to the display
            IFeatureLayer layer = new FeatureLayer();
            layer.FeatureClass = createdFeatureClass;
            layer.Name = createdFeatureClass.AliasName;
            layer.DisplayField = "HistoField";
            
            RenderFeatures(layer);

            //Add the layer to the map
            ArcMap.Document.FocusMap.AddLayer(layer);

        }

        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }

        private void BoboDataGeneration(IFeatureClass featureClass, IFeatureWorkspace featureWorkspace)
        {
            ((IWorkspaceEdit)featureWorkspace).StartEditing(true);
            ((IWorkspaceEdit)featureWorkspace).StartEditOperation();
            
            IFeatureCursor featureCursor = featureClass.Insert(false);
            int XCoord;
            int YCoord;
            int histValue;
            Random random = new Random();

            for(int i = 0; i < 1000; i++)
            {
                //Generate random values for points and for point values
                
                XCoord = random.Next(-179, 179);
                YCoord = random.Next(-89, 89);
                histValue = random.Next(1, 255);


                int histoGramData = featureCursor.Fields.FindField("HistoField");
                //Andrew Method
                //IFeature f = featureClass.CreateFeature();
                //f.Value[histoGramData] = histValue;
                //f.Shape = new Point() {X = XCoord, Y = YCoord};
                //f.Store();
                //Nohe method
                IFeatureBuffer featureBuffer = featureClass.CreateFeatureBuffer();
                featureBuffer.Value[histoGramData] = histValue;
                featureBuffer.Shape = new Point() { X = XCoord, Y = YCoord };

                featureCursor.InsertFeature(featureBuffer);


            }
            //featureCursor.Flush();
            ((IWorkspaceEdit)featureWorkspace).StopEditOperation();
            ((IWorkspaceEdit) featureWorkspace).StopEditing(true);
        }

        private IFeatureClass CreateFeatureClass(string Name, IFeatureWorkspace FeatureWorkspace)
        {
            //The feature that will be returned
            IFeatureClass featureClassCreated;

            //Create the filed for the histogram and the fields to be created in the future class
            IObjectClassDescription objectClassDescription = new FeatureClassDescription();
            IFields fields = objectClassDescription.RequiredFields;
            IFieldsEdit fieldsEdit = fields as IFieldsEdit;
            IField field = new Field();
            IFieldEdit fieldEdit = field as IFieldEdit;
            fieldEdit.AliasName_2 = "HistoField";
            fieldEdit.Name_2 = "HistoField";
            fieldEdit.Editable_2 = true;
            fieldEdit.Type_2 = esriFieldType.esriFieldTypeInteger;
            fieldsEdit.AddField(field);
            fields = fieldsEdit as IFields;

            //Create and assugn a CLSID
            UID CLSID = new UIDClass();
            CLSID.Value = "esriGeodatabase.Feature";

            string strShapeField = "";

            //Find the geometry field and then set the spatial reference and the geometry type.
            for (int i = 0; i < fields.FieldCount; i++)
            {
                if (fields.get_Field(i).Type == esriFieldType.esriFieldTypeGeometry)
                {
                    strShapeField = fields.get_Field(i).Name;
                    IGeometryDef geomDef = fields.get_Field(i).GeometryDef;
                    IGeometryDefEdit geomDefEdit = (IGeometryDefEdit)geomDef;
                    geomDefEdit.SpatialReference_2 = getSpatialReference(4326);
                    geomDefEdit.GeometryType_2 = esriGeometryType.esriGeometryPoint;
                    break;
                }
            }

            //If the file exists, overwrite it, otherwise create a new one.
            if (((IWorkspace2)FeatureWorkspace).NameExists[esriDatasetType.esriDTFeatureClass, Name])
            {

                IDataset dataset = FeatureWorkspace.OpenFeatureClass(Name) as IDataset;
                dataset.Delete();
                featureClassCreated = FeatureWorkspace.CreateFeatureClass(Name, fields, CLSID, null, esriFeatureType.esriFTSimple, strShapeField, "");
            }
            else
            {
                featureClassCreated = FeatureWorkspace.CreateFeatureClass(Name, fields, CLSID, null, esriFeatureType.esriFTSimple, strShapeField, "");
            }
            return featureClassCreated;
        }

        //Broke this out to make it look a little cleaner up top.
        private ISpatialReference getSpatialReference(int factoryCode)
        {
            ISpatialReferenceFactory spatialReferenceFactory = new SpatialReferenceEnvironmentClass();
            ISpatialReference spatialReference = (ISpatialReference)spatialReferenceFactory.CreateGeographicCoordinateSystem(factoryCode);
            return spatialReference;
        }

        private void RenderFeatures(ILayer layer)
        {
            //Set up renderer
            IClassBreaksRenderer classBreaksRenderer = new ClassBreaksRenderer();
            classBreaksRenderer.Field = "HistoField";
            classBreaksRenderer.BreakCount = 5;

            //Set up table histogram properties
            object douleArrayValues;
            object frequencyArray;
            IFeatureClass featureClass = ((IFeatureLayer) layer).FeatureClass;
            ITable table = (ITable) featureClass;
            ITableHistogram tableHistogram = (ITableHistogram) new BasicTableHistogram();
            tableHistogram.Table = table;
            tableHistogram.Field = "HistoField";
            ((IDataSampling)classBreaksRenderer).SamplingMethod = esriDataSampling.esriAllRecords;
            tableHistogram.Sampling = (IDataSampling)classBreaksRenderer;
            ((IBasicHistogram) tableHistogram).GetHistogram(out douleArrayValues, out frequencyArray);
            IClassifyGEN classifyGen = new NaturalBreaks();
            classifyGen.Classify(douleArrayValues, frequencyArray, classBreaksRenderer.BreakCount);
            Double[] x = classifyGen.ClassBreaks as Double[];
            Random random = new Random();
            for (var i = 1; i < x.Length; i++)
            {
                classBreaksRenderer.Break[i-1] = x[i];
                classBreaksRenderer.Description[i-1] = "TEST";
                classBreaksRenderer.Label[i-1] = x.GetValue(i).ToString();
                IMarkerSymbol markerSymbol = new SimpleMarkerSymbol();
                Color colorToUse = GetAColor(random.Next(0,174));
                IRgbColor rgbColor = new RgbColorClass();
                rgbColor.Blue = colorToUse.B;
                rgbColor.Red = colorToUse.R;
                rgbColor.Green = colorToUse.G;
                markerSymbol.Color = rgbColor;
                markerSymbol.Size = 5;
                classBreaksRenderer.Symbol[i - 1] = (ISymbol)markerSymbol;
            }

            ((IGeoFeatureLayer) layer).Renderer = ((IFeatureRenderer)classBreaksRenderer);
        }

        private Color GetAColor(int colorInt)
        {
            
            
            KnownColor[] colors = (KnownColor[]) Enum.GetValues(typeof(KnownColor));
            foreach (KnownColor knowColor in colors)
            {
                Color color = Color.FromKnownColor(knowColor);
            }
            //MessageBox.Show(colors.Length.ToString());

            KnownColor knownColor = colors[colorInt];
            Color colorToUse = Color.FromKnownColor(knownColor);

            return colorToUse;
        }

    }

}
