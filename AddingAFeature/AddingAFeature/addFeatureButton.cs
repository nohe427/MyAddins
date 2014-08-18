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

           // Nohe did this
            //IDocument doc = ArcMap.Application.Document;
            //IMxDocument mxDoc = doc as IMxDocument;
            //int value = ArcMap.Application.hWnd;

            //IActiveView av = mxDoc.ActiveView as IActiveView;
            //IMap map = mxDoc.FocusMap as IMap;
           
           //frddie
            IMap map = ArcMap.Document.ActiveView.FocusMap;
            Type factoryType = Type.GetTypeFromProgID("esriDataSourcesGDB.FileGDBWorkspaceFactory");
           
           IWorkspaceFactory wsf = Activator.CreateInstance(factoryType) as IWorkspaceFactory;
           //nohe
            //IWorkspaceFactory wsf = new FileGDBWorkspaceFactory();
            IFeatureWorkspace ws = wsf.OpenFromFile(@"C:\Users\alex7370\Documents\GitHub\MyAddins\AddingAFeature\features.gdb", 0) as IFeatureWorkspace;
            IFeatureLayer featureLayer = new FeatureLayerClass { FeatureClass = ws.OpenFeatureClass("pointFeature")};
            featureLayer.Name = featureLayer.FeatureClass.AliasName;
            
            map.AddLayer(featureLayer);
            ArcMap.Document.ActiveView.Refresh();
        }
    }

}
