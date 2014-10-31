using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace reportGenerator
{
    public partial class ReportGenerator : Form
    {
        string username;
        string password;
        string token;
        string storageLocation;
        string zipCode;
        string status;

        public ReportGenerator()
        {
            InitializeComponent();
        }

        private void logonButton_Click(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = "Logging into ArcGIS Online...";
            username = usernameTextBox.Text;
            password = passwordTextBox.Text;

            if (username == "" || password == "")
            {
                toolStripStatusLabel1.Text = "Please provide your credentials...";
            }
            else
            {
                AGOL agol = new AGOL(username, password);
                token = agol.Token;
                Console.WriteLine(token);
                toolStripStatusLabel1.Text = "Token generated... Login success!";
                Console.WriteLine(agol.orgInfo.id);
            }
        }

        private void getReportsButton_Click(object sender, EventArgs e)
        {
            toolStripStatusLabel1.Text = "Running reports...";
            storageLocation = storageLocationTextBox.Text;
            zipCode = zipCodeTextBox.Text;

            if (zipCode == "" || storageLocation == "")
            {
                toolStripStatusLabel1.Text = "You need to enter information...";
            }
            else
            {
                
                status = pdfCreator("dandi", dandiCheckBox.Checked);
                toolStripStatusLabel1.Text = status;
                status = pdfCreator("census2010_profile", census2010CheckBox.Checked);
                toolStripStatusLabel1.Text = status;
                status = pdfCreator("business_summary", businessSummaryCheckBox.Checked);
                toolStripStatusLabel1.Text = status;
            }
        }

        private string pdfCreator(string reportType, bool status)
        {
            string report = reportName(reportType);

            if (status == true)
            {
                using (WebClient client = new WebClient())
                {
                    client.DownloadFile("http://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/GeoEnrichment/CreateReport?studyAreas=[{%22sourceCountry%22:%22US%22,%22layer%22:%22US.ZIP5%22,%22ids%22:[%22" + zipCode + "%22]}]&report=" + reportType + "&f=bin&token=" + token, storageLocation+report+".pdf");
                }
                return report + " has run";
            }
            else{
                return report + " was not selected so it was not run.";
            }
        }

        private string reportName(string reportCode)
        {
            string reportName = "";
            if (reportCode == "dandi")
            {
                reportName = "Demographic and Income Profile";
            }
            else if (reportCode == "census2010_profile")
            {
                reportName = "Census 2010 Profile";
            }
            else if (reportCode == "business_summary")
            {
                reportName = "Business Summary";
            }
            else
            {
                reportName = "Missing Report Name";
            }
            return reportName;
        }
    }
}
