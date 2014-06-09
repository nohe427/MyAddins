using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using ESRI.ArcGIS.ArcMapUI;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.Framework;

namespace TestAddIn
{
    public class LayersOfMapButton : ESRI.ArcGIS.Desktop.AddIns.Button
    {
        public LayersOfMapButton()
        {
        }

        protected override void OnClick()
        {
            string data = "";

            IDocument doc = ArcMap.Application.Document;
            IMxDocument mxDoc = doc as IMxDocument;

            IMap map = mxDoc.FocusMap;
            data += "Using LayerCount Property \n";

            ILayer layer;
            for (int i = 0; i < map.LayerCount; i++)
            {
                layer = map.Layer[i];
                bool visibility = layer.Visible;
                data += ">> " + layer.Name + "\n";
            }
            layer = null;
            data += string.Format( "{0} Map contains {1} Layers\n", map.Name, map.LayerCount);
            data += "---------------------------------------------------------------\n";
            data += "Using Layer Property \n";
            IEnumLayer enumLayer = map.Layers;
            layer = enumLayer.Next();
            int j = 0;
            while (layer != null)
            {
                j++;
                data += ">>" + layer.Name + "\n";
                layer = enumLayer.Next();
            }
            data += string.Format("{0} Map Contains {1} Layers", map.Name, j);

            Message msgFrom = new Message();
            msgFrom.label1.Text = data;
            msgFrom.ShowDialog();
        }
        protected override void OnUpdate()
        {
            Enabled = ArcMap.Application != null;
        }
    }

}
