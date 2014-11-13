using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfRuntimeAttempt
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void logonButton_Click(object sender, RoutedEventArgs e)
        {
            string username = Username.Text;
            string password = Password.Text;

            AGOL agol = new AGOL(username, password);

            int i;
            i = 0;
            foreach(var service in agol.orgServices.services)
            {
                CheckBox box = new CheckBox();
                box.Name = "A"+i.ToString();
                box.Content = service.name;
                box.Checked += async(s,ev) =>
                    {
                        //Having trouble with the token
                        var table = new Esri.ArcGISRuntime.Data.ServiceFeatureTable();
                        //table.Token = agol.Token;
                        //MessageBox.Show(agol.Token);
                        table.ServiceUri = service.url+"/0";
                        table.Where = "1=1";
                        Esri.ArcGISRuntime.Layers.FeatureLayer myFeatureLayer = new Esri.ArcGISRuntime.Layers.FeatureLayer();
                        myFeatureLayer.FeatureTable = table;
                        MyView.Map.Layers.Add(myFeatureLayer);
                        await myFeatureLayer.InitializeAsync();
                        Esri.ArcGISRuntime.ArcGISServices.FeatureServiceLayerInfo myFeatureServiceLayerInfo = table.ServiceInfo;
                        //var gdbFeatureSvcTable = await Esri.ArcGISRuntime.Data.ServiceFeatureTable.OpenAsync(
                        //    new Uri(service.url));
                        //gdbFeatureSvcTable.Mode = Esri.ArcGISRuntime.Data.QueryMode.OnDemand;
                        //gdbFeatureSvcTable.Where = "1=1";
                        //gdbFeatureSvcTable.Token = agol.Token;
                        //var featureLayer = new Esri.ArcGISRuntime.Layers.FeatureLayer(gdbFeatureSvcTable);
                        //featureLayer.ID = box.Name;
                        //MyView.Map.Layers.Add(featureLayer);
                        //var dynUri = new Uri(service.url + agol.Token);
                        //var agsDynLayer = new Esri.ArcGISRuntime.Layers.ArcGISDynamicMapServiceLayer(dynUri);
                        //MyView.Map.Layers.Add(agsDynLayer);
                    };
                box.Unchecked += (s, ev) =>
                {
                    MessageBox.Show("SOMETHING");
                };
                servicesBox.Items.Add(box);
                i++;
            }
        }
    }
}
