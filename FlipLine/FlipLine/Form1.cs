using ESRI.ArcGIS.Geodatabase;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Text;
using System.Windows.Forms;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Catalog;
using ESRI.ArcGIS.CatalogUI;
using ESRI.ArcGIS.Controls;
using ESRI.ArcGIS.Display;
using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Editor;
using ESRI.ArcGIS.Geometry;
using Path = System.IO.Path;

namespace FlipLine
{
    public partial class Form1 : Form
    {
        private IEngineEditor m_engineEditor = new EngineEditorClass();
        private static Type fileGdbType = Type.GetTypeFromProgID("esriDataSourcesGDB.FileGDBWorkspaceFactory");
        private static IWorkspaceFactory fileWorkspaceFactory = Activator.CreateInstance(fileGdbType) as IWorkspaceFactory;

        private static IFeatureLayer layer;
        private static Type sdeType = Type.GetTypeFromProgID("esriDataSourcesGDB.SdeWorkspaceFactory");
        private static IWorkspaceFactory sdeWorkspaceFactory = Activator.CreateInstance(sdeType) as IWorkspaceFactory;
        private IFeatureClass featureClass;

        public Form1()
        {
            InitializeComponent();
        }

        private void exit_button_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void default_button_Click(object sender, EventArgs e)
        {
            IFeatureWorkspace featureWorkspace = fileWorkspaceFactory.OpenFromFile(Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "Data", "SampleData.gdb"), 0) as IFeatureWorkspace;
            dataViewerMapControl.ActiveView.FocusMap.ClearLayers();
            layer = new FeatureLayer();
            layer.Name = "Sample Data";
            layer.FeatureClass = featureWorkspace.OpenFeatureClass("TestData");
            dataViewerMapControl.AddLayer(layer);
            featureClass = layer.FeatureClass;
            populateOIDBox(layer.FeatureClass);
        }

        private void load_button_Click(object sender, EventArgs e)
        {
            IGxDialog gxDialog = new GxDialog();
            gxDialog.AllowMultiSelect = false;
            gxDialog.ObjectFilter = new GxFilterPolylineFeatureClasses();
            gxDialog.Title = "Select your polyline features";
            IEnumGxObject objEnumerator = null;
            gxDialog.DoModalOpen(0, out objEnumerator);
            if (objEnumerator.Next() == null) return;
            objEnumerator.Reset();

            dataViewerMapControl.ActiveView.FocusMap.ClearLayers();

            IGxDataset gxDataset = objEnumerator.Next() as IGxDataset;
            IFeatureWorkspace workspace = gxDataset.Dataset.Workspace.PathName.EndsWith(".sde")
                ? sdeWorkspaceFactory.OpenFromFile(gxDataset.Dataset.Workspace.PathName, 0) as IFeatureWorkspace
                : fileWorkspaceFactory.OpenFromFile(gxDataset.Dataset.Workspace.PathName, 0) as IFeatureWorkspace;

            layer = new FeatureLayerClass();
            layer.FeatureClass = workspace.OpenFeatureClass(gxDataset.DatasetName.Name);
            layer.Name = gxDataset.DatasetName.Name;
            dataViewerMapControl.AddLayer(layer);
            featureClass = layer.FeatureClass;
            populateOIDBox(layer.FeatureClass);
        } 

        private void flip_button_Click(object sender, EventArgs e)
        {
            StartEditing(dataViewerMapControl.GetOcx() as IMapControl2);

            IFeature feature = featureClass.GetFeature(Int32.Parse(objectIDListBox.SelectedItem.ToString()));
            IPolyline6 curve = feature.Shape as IPolyline6;
            curve.ReverseOrientation();
            feature.Shape = curve;
            feature.Store();

            StopEditing(dataViewerMapControl.GetOcx() as IMapControl2);
            layer.FeatureClass = featureClass;
            objectIDListBox_SelectedIndexChanged(new object(), new EventArgs());
        }

        private void previous_button_Click(object sender, EventArgs e)
        {
            if (objectIDListBox.SelectedIndex > 0)
            {
                objectIDListBox.SelectedIndex--;
            }
        }

        private void next_button_Click(object sender, EventArgs e)
        {
            if (objectIDListBox.SelectedIndex == -1)
            {
                objectIDListBox.SelectedIndex = 0;
            }
            else
            {
                if (objectIDListBox.SelectedIndex < objectIDListBox.Items.Count-1)
                {
                    objectIDListBox.SelectedIndex++;
                }
            }
        }

        private void populateOIDBox(IFeatureClass featureClass)
        {
            IFeatureCursor featureCursor = featureClass.Search(new QueryFilterClass(), true);
            objectIDListBox.Items.Clear();
            IFeature feature = featureCursor.NextFeature();
            while (feature != null)
            {
                objectIDListBox.Items.Add(feature.OID.ToString());
                feature = featureCursor.NextFeature();
            }
            Marshal.FinalReleaseComObject(featureCursor);

        }

        private void objectIDListBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            int selectedOID = Int32.Parse(objectIDListBox.SelectedItem.ToString());
            IFeature feature = featureClass.GetFeature(selectedOID);

            ESRI.ArcGIS.Carto.IGraphicsContainer graphicsContainer =
                (ESRI.ArcGIS.Carto.IGraphicsContainer) dataViewerMapControl.Map;
            graphicsContainer.DeleteAllElements();

            AddGraphicToMap(dataViewerMapControl.Map, ((IPolyline)feature.Shape).FromPoint, new RgbColorClass() { Green = 255 }, new RgbColorClass() { Green = 255 });
            AddGraphicToMap(dataViewerMapControl.Map, ((IPolyline)feature.Shape).ToPoint, new RgbColorClass() { Red = 255 }, new RgbColorClass() { Red = 255 });

            dataViewerMapControl.Extent = feature.Extent;
            dataViewerMapControl.Refresh();
        }

        public void AddGraphicToMap(ESRI.ArcGIS.Carto.IMap map, ESRI.ArcGIS.Geometry.IGeometry geometry, ESRI.ArcGIS.Display.IRgbColor rgbColor, ESRI.ArcGIS.Display.IRgbColor outlineRgbColor)
        {
            ESRI.ArcGIS.Carto.IGraphicsContainer graphicsContainer = (ESRI.ArcGIS.Carto.IGraphicsContainer)map; // Explicit Cast
            ESRI.ArcGIS.Carto.IElement element = null;
            if ((geometry.GeometryType) == ESRI.ArcGIS.Geometry.esriGeometryType.esriGeometryPoint)
            {
                // Marker symbols
                ESRI.ArcGIS.Display.ISimpleMarkerSymbol simpleMarkerSymbol = new ESRI.ArcGIS.Display.SimpleMarkerSymbolClass();
                simpleMarkerSymbol.Color = rgbColor;
                simpleMarkerSymbol.Outline = true;
                simpleMarkerSymbol.OutlineColor = outlineRgbColor;
                simpleMarkerSymbol.Size = 15;
                simpleMarkerSymbol.Style = ESRI.ArcGIS.Display.esriSimpleMarkerStyle.esriSMSCircle;

                ESRI.ArcGIS.Carto.IMarkerElement markerElement = new ESRI.ArcGIS.Carto.MarkerElementClass();
                markerElement.Symbol = simpleMarkerSymbol;
                element = (ESRI.ArcGIS.Carto.IElement)markerElement; // Explicit Cast
            }
            else if ((geometry.GeometryType) == ESRI.ArcGIS.Geometry.esriGeometryType.esriGeometryPolyline)
            {
                //  Line elements
                ESRI.ArcGIS.Display.ISimpleLineSymbol simpleLineSymbol = new ESRI.ArcGIS.Display.SimpleLineSymbolClass();
                simpleLineSymbol.Color = rgbColor;
                simpleLineSymbol.Style = ESRI.ArcGIS.Display.esriSimpleLineStyle.esriSLSSolid;
                simpleLineSymbol.Width = 5;

                ESRI.ArcGIS.Carto.ILineElement lineElement = new ESRI.ArcGIS.Carto.LineElementClass();
                lineElement.Symbol = simpleLineSymbol;
                element = (ESRI.ArcGIS.Carto.IElement)lineElement; // Explicit Cast
            }
            else if ((geometry.GeometryType) == ESRI.ArcGIS.Geometry.esriGeometryType.esriGeometryPolygon)
            {
                // Polygon elements
                ESRI.ArcGIS.Display.ISimpleFillSymbol simpleFillSymbol = new ESRI.ArcGIS.Display.SimpleFillSymbolClass();
                simpleFillSymbol.Color = rgbColor;
                simpleFillSymbol.Style = ESRI.ArcGIS.Display.esriSimpleFillStyle.esriSFSForwardDiagonal;
                ESRI.ArcGIS.Carto.IFillShapeElement fillShapeElement = new ESRI.ArcGIS.Carto.PolygonElementClass();
                fillShapeElement.Symbol = simpleFillSymbol;
                element = (ESRI.ArcGIS.Carto.IElement)fillShapeElement; // Explicit Cast
            }
            if (!(element == null))
            {
                element.Geometry = geometry;
                graphicsContainer.AddElement(element, 0);
            }
        }

        private void StartEditing(IMapControl2 m_mapControl)
        {
            IMap map = m_mapControl.Map;

            //If an edit session has already been started, exit.
            if (m_engineEditor.EditState != esriEngineEditState.esriEngineStateNotEditing)
                return;

            //Start editing the workspace of the first feature layer found.
            for (int layerCounter = 0; layerCounter <= map.LayerCount - 1; layerCounter++)
            {
                ILayer currentLayer = map.get_Layer(layerCounter);
                if (currentLayer is IFeatureLayer)
                {
                    IFeatureLayer featureLayer = currentLayer as IFeatureLayer;
                    IDataset dataset = featureLayer.FeatureClass as IDataset;
                    IWorkspace workspace = dataset.Workspace;
                    m_engineEditor.StartEditing(workspace, map);
                    ((IEngineEditLayers)m_engineEditor).SetTargetLayer(featureLayer, 0);
                    break;
                }
            }
        }

        private void StopEditing(IMapControl2 mapControl)
        {
            if (MessageBox.Show("Save Edits?", "Save Prompt", MessageBoxButtons.YesNo)
           == DialogResult.Yes)
                m_engineEditor.StopEditing(true);
            else
                m_engineEditor.StopEditing(false);
        }
        
    }
}