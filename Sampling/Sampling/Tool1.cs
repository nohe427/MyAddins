using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Sampling
{
    public class Tool1 : ESRI.ArcGIS.Desktop.AddIns.Tool
    {
        public Tool1()
        {
        }

        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }
    }

}
