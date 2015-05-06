using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Reflection;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Geodatabase;

namespace EndPointsAddin
{
    public class AddsTheData : ESRI.ArcGIS.Desktop.AddIns.Extension
    {
        public AddsTheData()
        {
        }

        protected override void OnStartup()
        {
            //
            // TODO: Uncomment to start listening to document events
            //
            WireDocumentEvents();
        }

        private void WireDocumentEvents()
        {
            //
            // TODO: Sample document event wiring code. Change as needed
            //

            // Named event handler
            ArcMap.Events.NewDocument += ArcMap_NewDocument;

            
            // Anonymous event handler
            /*
            ArcMap.Events.BeforeCloseDocument += delegate()
            {
                // Return true to stop document from closing
                ESRI.ArcGIS.Framework.IMessageDialog msgBox = new ESRI.ArcGIS.Framework.MessageDialogClass();
                return msgBox.DoModal("BeforeCloseDocument Event", "Abort closing?", "Yes", "No", ArcMap.Application.hWnd);
            };
             * 
             */

        }

        private void ArcMap_NewDocument()
        {
            // TODO: Handle new document event

            IMap map = ArcMap.Document.FocusMap;

            Type factoryType = Type.GetTypeFromProgID("esriDataSourcesGDB.FileGDBWorkspaceFactory");
            IWorkspaceFactory workspaceFactory = Activator.CreateInstance(factoryType) as IWorkspaceFactory;
            IWorkspace workspace = workspaceFactory.OpenFromFile(Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location) ,@"Data\PointsToAdd.gdb"), 0);
            IFeatureWorkspace featureWorkspace = workspace as IFeatureWorkspace;
            IFeatureClass featureClassLines = featureWorkspace.OpenFeatureClass("Lines");
            IFeatureClass featureClassPoints = featureWorkspace.OpenFeatureClass("Points");

            IFeatureLayer featureLayerLines = new FeatureLayer();
            IFeatureLayer featureLayerPoints = new FeatureLayer();

            featureLayerLines.FeatureClass = featureClassLines;
            featureLayerPoints.FeatureClass = featureClassPoints;
            featureLayerPoints.Name = "Points";
            featureLayerLines.Name = "Lines";

            map.AddLayer(featureLayerPoints);
            map.AddLayer(featureLayerLines);
            map.RecalcFullExtent();
            
        }

    }

}
