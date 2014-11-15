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
using Esri.ArcGISRuntime;
using Newtonsoft.Json;
using System.Collections.Specialized;
using System.Net;

namespace CustomTokenRuntime
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

        private string _getResponse(NameValueCollection data, string url)
        {
            string responseData;
            var webClient = new WebClient();
            var response = webClient.UploadValues(url, data);
            responseData = System.Text.Encoding.UTF8.GetString(response);
            return responseData;
        }

        public string GetToken(string username, string password)
        {

            var data = new NameValueCollection();
            data["username"] = username;
            data["password"] = password;
            data["referer"] = "https://www.arcgis.com";
            data["f"] = "json";

            TokenInfo x = JsonConvert.DeserializeObject<TokenInfo>(_getResponse(data, "https://arcgis.com/sharing/rest/generateToken"));
            return x.token; ;
        }

        public class TokenInfo
        {
            public string token { get; set; }
            public long expires { get; set; }
            public bool ssl { get; set; }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            //Please insert your username and password below.  Make sure that they are part of the ESS organization.
            string username = "";
            string password = "";
            string serviceUrl = "http://services.arcgis.com/Wl7Y1m92PbjtJs5n/arcgis/rest/services/brainCarsonONTIME/FeatureServer/";

            string token = GetToken(username, password);

            addLayer(token, serviceUrl);

        }

        public void addLayer(string token, string serviceUrl)
        {
            //Uncomment the workaround line to see the workaround work.
            //Workaround(serviceUrl, token);
            var table = new Esri.ArcGISRuntime.Data.ServiceFeatureTable();
            table.Token = token;
            table.ServiceUri = serviceUrl + "0";
            table.Where = "1=1";
            Esri.ArcGISRuntime.Layers.FeatureLayer myFeatureLayer = new Esri.ArcGISRuntime.Layers.FeatureLayer();
            myFeatureLayer.FeatureTable = table;
            MyView.Map.Layers.Add(myFeatureLayer);
            myFeatureLayer.InitializeAsync();
            Esri.ArcGISRuntime.ArcGISServices.FeatureServiceLayerInfo myFeatureServiceLayerInfo = table.ServiceInfo;
        }

        public void Workaround(string url, string token)
        {
            var data = new NameValueCollection();
            data["token"] = token;
            data["f"] = "json";

            var webClient = new WebClient();
            webClient.UploadValues(url, data);
        }
    }
}
