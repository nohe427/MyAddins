using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

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
            ArcMap.Application.CurrentTool = null;
        }
        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }
    }

}
