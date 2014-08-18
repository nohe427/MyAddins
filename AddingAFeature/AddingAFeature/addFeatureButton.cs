using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.DataSourcesGDB;
using ESRI.ArcGIS.Framework;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.ArcMapUI;

namespace AddingAFeature
{
    public class addFeatureButton : ESRI.ArcGIS.Desktop.AddIns.Button
    {
        public addFeatureButton()
        {
        }

        protected override void OnClick()
        {
            //
            //  TODO: Sample code showing how to access button host
            //
            // ArcMap.Application.CurrentTool = null;
            IDocument doc = ArcMap.Application.Document;
            IMxDocument mxDoc = doc as IMxDocument;
            int value = ArcMap.Application.hWnd;

            IActiveView av = mxDoc.ActiveView as IActiveView;
            IMap map = mxDoc.FocusMap as IMap;
            
            IWorkspaceFactory wsf = new FileGDBWorkspaceFactory();
            IFeatureWorkspace ws = wsf.OpenFromFile("C:\\Users\\AlexanderN\\Documents\\GitHub\\MyAddins\\AddingAFeature\\features.gdb", value) as IFeatureWorkspace;
            IFeatureLayer featureLayer = new FeatureLayerClass();
            featureLayer.FeatureClass = ws.OpenFeatureClass("pointFeature");
            ILayer layer = (ILayer)featureLayer;
            layer.Name = featureLayer.FeatureClass.AliasName;
            
            map.AddLayer(layer);
            av.Refresh();
        }
        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }
    }

}
