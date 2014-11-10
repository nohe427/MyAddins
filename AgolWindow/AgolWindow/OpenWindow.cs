using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Framework;

namespace AgolWindow
{
    public class OpenWindow : ESRI.ArcGIS.Desktop.AddIns.Button
    {
        public OpenWindow()
        {
        }

        protected override void OnClick()
        {
            //
            //  TODO: Sample code showing how to access button host
            //
            UID dockWinID = new UIDClass();
            dockWinID.Value = ThisAddIn.IDs.AGOLWindow;

            // Use GetDockableWindow directly as we want the client IDockableWindow not the internal class  
            IDockableWindow dockWindow = ArcMap.DockableWindowManager.GetDockableWindow(dockWinID);
            dockWindow.Show(true);  
        }
        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }
    }

}
