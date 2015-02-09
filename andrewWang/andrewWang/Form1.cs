using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Geodatabase;

namespace andrewWang
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void mapsComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            int selectedMap = mapsComboBox.SelectedIndex;
            axMapControl1.ActiveView.Clear();
            axMapControl1.LoadMxFile(@"C:\Program Files (x86)\ArcGIS\DeveloperKit10.2\Samples\data\California\California.mxd", selectedMap,null);
            IEnumLayer layers = axMapControl1.ActiveView.FocusMap.Layers;
            ILayer L = layers.Next();
            while (L != null)
            {
                layersListBox.Items.Add(L.Name);
                L = layers.Next();
            }
        }

        private void loadMXDOCBbutton_Click(object sender, EventArgs e)
        {
            IMapDocument mapDox = new MapDocument();
            mapDox.Open(@"C:\Program Files (x86)\ArcGIS\DeveloperKit10.2\Samples\data\California\California.mxd");
            for (int i = 0; i < mapDox.MapCount; i++)
            {
                mapsComboBox.Items.Add(mapDox.get_Map(i).Name);
            }
        }

        private void layersListBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            fieldListBox.Items.Clear();
            IFeatureLayer layers = axMapControl1.ActiveView.FocusMap.Layer[layersListBox.SelectedIndex] as IFeatureLayer;
            IFields fields = layers.FeatureClass.Fields;
            for (int i = 0; i < fields.FieldCount; i++)
            {
                fieldListBox.Items.Add(fields.Field[i].Name);
            }
        }



    }
}