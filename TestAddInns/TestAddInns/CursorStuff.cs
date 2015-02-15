using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Windows.Forms;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Geometry;
using ESRI.ArcGIS.Geodatabase;

namespace TestAddInns
{
    public class CursorStuff : ESRI.ArcGIS.Desktop.AddIns.Button
    {
        public CursorStuff()
        {
        }

        protected override void OnClick()
        {
            //
            //  TODO: Sample code showing how to access button host
            //
            ArcMap.Application.CurrentTool = null;
            ILayer layer = ArcMap.Document.SelectedLayer as ILayer;
            ILayer2 layer3 = layer as ILayer2;
            IGeometry layer2 = layer as IGeometry;
            IFeatureLayer2 classLayer = layer as IFeatureLayer2;
            classLayer.
            MessageBox.Show(classLayer.DisplayField.ToString());
        }
        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }
    }

}
