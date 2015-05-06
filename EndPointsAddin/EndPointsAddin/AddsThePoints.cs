using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Windows.Forms;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Editor;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.Geometry;

namespace EndPointsAddin
{
    /// <summary>
    /// AddsThePoints class implementing custom ESRI Editor Extension functionalities.
    /// </summary>
    public class AddsThePoints : ESRI.ArcGIS.Desktop.AddIns.Extension
    {
        private IEditor theEditor;
        public AddsThePoints()
        {
        }

        protected override void OnStartup()
        {
            theEditor = ArcMap.Editor;
            WireEditorEvents();
        }

        protected override void OnShutdown()
        {
        }

        #region Editor Events

        #region Shortcut properties to the various editor event interfaces
        private IEditEvents_Event Events
        {
            get { return ArcMap.Editor as IEditEvents_Event; }
        }
        private IEditEvents2_Event Events2
        {
            get { return ArcMap.Editor as IEditEvents2_Event; }
        }
        private IEditEvents3_Event Events3
        {
            get { return ArcMap.Editor as IEditEvents3_Event; }
        }
        private IEditEvents4_Event Events4
        {
            get { return ArcMap.Editor as IEditEvents4_Event; }
        }
        #endregion

        void WireEditorEvents()
        {
            //
            //  TODO: Sample code demonstrating editor event wiring
            //

            //Events.OnCurrentTaskChanged += delegate
            //{
            //    if (ArcMap.Editor.CurrentTask != null)
            //        System.Diagnostics.Debug.WriteLine(ArcMap.Editor.CurrentTask.Name);
            //};

            //Events2.BeforeStopEditing += delegate(bool save) { OnBeforeStopEditing(save); };

            Events.OnCreateFeature += new IEditEvents_OnCreateFeatureEventHandler(OnCreationFinishedGenesis);
        }

        private void OnCreationFinishedGenesis(IObject obj)
        {
            ISpatialFilter spatialFilter = new SpatialFilter();
            spatialFilter.SpatialRel = esriSpatialRelEnum.esriSpatialRelIntersects;

            
            
            IGeometry geometryOfFeature = ((IFeature) obj).Shape;
            if (geometryOfFeature.GeometryType == esriGeometryType.esriGeometryPolyline)
            {
                IPoint pointStart = ((IPolyline) geometryOfFeature).ToPoint;
                IPoint pointEnd = ((IPolyline) geometryOfFeature).FromPoint;
                //MessageBox.Show(String.Format("The starting X: {0} and y:{1}", pointStart.X, pointStart.Y));
                //MessageBox.Show(String.Format("The ending X: {0} and y:{1}", pointEnd.X, pointEnd.Y));

                IFeatureLayer pointLayer = (IFeatureLayer) GetPointFeature();


                ITable table = ((IFeature) obj).Table;
                IFeatureClass fc = table as IFeatureClass;
                if ((fc.AliasName) == "Lines")
                {
                    spatialFilter.Geometry = pointStart;
                    spatialFilter.GeometryField = fc.ShapeFieldName;

                    IFeatureCursor allPoints = (pointLayer.FeatureClass).Search(spatialFilter, false);
                    IFeature point = null;
                    if (allPoints.NextFeature() == null)
                    {
                        IFeature featureInsert = (pointLayer.FeatureClass).CreateFeature();
                        featureInsert.Shape = pointStart;
                        featureInsert.Store();
                    }

                    spatialFilter.Geometry = pointEnd;
                    spatialFilter.GeometryField = fc.ShapeFieldName;

                    allPoints = (pointLayer.FeatureClass).Search(spatialFilter, false);
                    point = null;
                    if (allPoints.NextFeature() == null)
                    {
                        IFeature featureInsert = (pointLayer.FeatureClass).CreateFeature();
                        featureInsert.Shape = pointEnd;
                        featureInsert.Store();
                        
                    }
                    allPoints.Flush();

                    //spatialFilter.Geometry = ((IFeature) pointLayer.FeatureClass).ShapeCopy;
                    //spatialFilter.GeometryField = fc.ShapeFieldName;

                    //IFeatureCursor featureCursor = ((IFeatureClass) pointStart).Search(spatialFilter, false);
                    //IFeature pointsInCursor = null;
                    //while ((pointsInCursor = featureCursor.NextFeature()) != null)
                    //{
                    //    MessageBox.Show(pointsInCursor.get_Value(0));
                    //}
                }
            }

        }

        private ILayer GetPointFeature()
        {
            ILayer layer = new FeatureLayer();
            IMap map = ArcMap.Document.FocusMap;
            for (int i = 0; i < map.LayerCount; i++)
            {
                if (map.Layer[i].Name == "Points")
                
                    layer = map.Layer[i];
                
            }
            return layer;
        }

        void OnBeforeStopEditing(bool save)
        {
            
        }
        #endregion

    }

}
