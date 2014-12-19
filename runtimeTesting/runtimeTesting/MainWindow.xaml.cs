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
using Esri.ArcGISRuntime.Geometry;
using Esri.ArcGISRuntime.Layers;
using Esri.ArcGISRuntime.Symbology;
using Esri.ArcGISRuntime.Tasks.Geocoding;
using Esri.ArcGISRuntime.Tasks.NetworkAnalyst;

namespace runtimeTesting
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            licenseMe();
            InitializeComponent();
        }

        private async void natigationButton_Click(object sender, RoutedEventArgs e)
        {
            var to = await FindAddress(toAddress.Text);
            var from = await FindAddress(fromAddress.Text);

            try
            {
                if (from == null)
                {
                    throw new Exception("Unable to find a match for '" + this.fromAddress.Text + "'.");
                }

                if (to == null)
                {
                    throw new Exception("Unable to find a match for '" + this.toAddress.Text + "'.");
                }

                // get the RouteResults graphics layer; add the from/to graphics
                var routeGraphics = Map.Layers["RouteResults"] as GraphicsLayer;
                if (routeGraphics == null)
                {
                    throw new Exception("A graphics layer named 'RouteResults' was not found in the map.");
                }

                // code here to show address locations on the map
                var fromMapPoint = GeometryEngine.Project(from.Geometry, new SpatialReference(102100));
                var toMapPoint = GeometryEngine.Project(to.Geometry, new SpatialReference(102100));

                var fromSym = new SimpleMarkerSymbol { Style = SimpleMarkerStyle.Circle, Size = 16, Color = Colors.Green };
                var toSym = new SimpleMarkerSymbol { Style = SimpleMarkerStyle.Circle, Size = 16, Color = Colors.Red };

                var fromMapGraphic = new Graphic { Geometry = fromMapPoint, Symbol = fromSym };
                var toMapGraphic = new Graphic { Geometry = toMapPoint, Symbol = toSym };

                routeGraphics.Graphics.Add(fromMapGraphic);
                routeGraphics.Graphics.Add(toMapGraphic);

                var uri = new Uri(
    "http://tasks.arcgisonline.com/ArcGIS/rest/services/NetworkAnalysis/ESRI_Route_NA/NAServer/Route"
    );
                var routeTask = new OnlineRouteTask(uri);

                var routeParams = await routeTask.GetDefaultParametersAsync();
                routeParams.OutSpatialReference = View.SpatialReference;
                routeParams.DirectionsLengthUnit = LinearUnits.Miles;
                routeParams.ReturnDirections = true;

                var stopGraphics = new List<Graphic>();
                stopGraphics.Add(from);
                stopGraphics.Add(to);
                routeParams.SetStops(stopGraphics);

                var routeResult = await routeTask.SolveAsync(routeParams);

                if (routeResult == null || routeResult.Routes == null || routeResult.Routes.Count == 0)
                {
                    throw new Exception("Unable to solve the route.");
                }

                var firstRoute = routeResult.Routes[0];

                var routeFeature = firstRoute.RouteFeature;
                var routeSym = new SimpleLineSymbol
                {
                    Color = Colors.Navy,
                    Style = SimpleLineStyle.Dash,
                    Width = 2
                };
                var routeGraphic = new Graphic(routeFeature.Geometry, routeSym);

                routeGraphics.Graphics.Add(routeGraphic);
                await View.SetViewAsync(routeGraphic.Geometry.Extent);

                var directionsBuilder = new System.Text.StringBuilder();
                var totalMiles = 0.0;
                var totalMinutes = 0.0;
                var step = 1;

                foreach (var d in firstRoute.RouteDirections)
                {
                    directionsBuilder.AppendFormat("{0} \t {1}", step.ToString(), d.Text + "\n");
                    step++;
                    totalMiles += d.GetLength(LinearUnits.Miles);
                    totalMinutes += d.Time.TotalMinutes;
                    this.RouteDistance.Content = totalMiles.ToString("0.00") + " miles";
                    this.RouteTime.Content = totalMinutes.ToString("0.00") + " minutes";
                    this.DirectionsTextBlock.Text = directionsBuilder.ToString();
                }
            }
            catch (Exception exp)
            {
                this.DirectionsTextBlock.Text = exp.Message;
            }
        }

        private void licenseMe()
        {
            Esri.ArcGISRuntime.ArcGISRuntimeEnvironment.ClientId = "";

            try
            {
                Esri.ArcGISRuntime.ArcGISRuntimeEnvironment.Initialize();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Unable to initialize the ArcGIS Runtime with the client id provided: " + ex.Message);
            }
        }

        private async System.Threading.Tasks.Task<Graphic> FindAddress(string address)
        {
            var uri = new Uri("http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer");
            var locator = new OnlineLocatorTask(uri, string.Empty);

            var findParams = new OnlineLocatorFindParameters(address);
            findParams.OutSpatialReference = new SpatialReference(4326);

            Graphic matchGraphic = null;
            var results = await locator.FindAsync(findParams, new System.Threading.CancellationToken());
            if (results.Count > 0)
            {
                var firstMatch = results[0].Feature;
                var matchLocation = firstMatch.Geometry as MapPoint;
                matchGraphic = new Graphic();
                matchGraphic.Geometry = matchLocation;
                matchGraphic.Attributes.Add("Name", address);
            }

            return matchGraphic;
        }
    }
}
