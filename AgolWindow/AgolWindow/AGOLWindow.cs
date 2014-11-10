using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace AgolWindow
{
    /// <summary>
    /// Designer class of the dockable window add-in. It contains user interfaces that
    /// make up the dockable window.
    /// </summary>
    public partial class AGOLWindow : UserControl
    {
        public AGOLWindow(object hook)
        {
            InitializeComponent();
            this.Hook = hook;
        }

        /// <summary>
        /// Host object of the dockable window
        /// </summary>
        private object Hook
        {
            get;
            set;
        }

        /// <summary>
        /// Implementation class of the dockable window add-in. It is responsible for 
        /// creating and disposing the user interface class of the dockable window.
        /// </summary>
        public class AddinImpl : ESRI.ArcGIS.Desktop.AddIns.DockableWindow
        {
            private AGOLWindow m_windowUI;

            public AddinImpl()
            {
            }

            protected override IntPtr OnCreateChild()
            {
                m_windowUI = new AGOLWindow(this.Hook);
                return m_windowUI.Handle;
            }

            protected override void Dispose(bool disposing)
            {
                if (m_windowUI != null)
                    m_windowUI.Dispose(disposing);

                base.Dispose(disposing);
            }

        }

        private void loginButton_Click(object sender, EventArgs e)
        {
            windowStatusLabel.Text = "Logging in...";
            string username = usernameTextBox.Text;
            string password = passwordTextBox.Text;
            try
            {
                AGOL agol = new AGOL(username, password);
                windowStatusLabel.Text = agol.Token.ToString();
                windowStatusLabel.Text = "Logged in!";

                string orgInfoString;
                windowStatusLabel.Text = "Getting organization information...";
                orgInfoString = "";
                orgInfoString += "Access: " + agol.orgInfo.access + "\n";
                orgInfoString += "Available Credits: " + agol.orgInfo.availableCredits + "\n";
                orgInfoString += "DatabaseUsage: " + agol.orgInfo.databaseUsage + "\n";
                orgInfoString += "ID: " + agol.orgInfo.id + "\n";
                orgInfoString += "Storage Usage: " + agol.orgInfo.storageUsage + "\n";
                orgInfoString += "URL Key: " + agol.orgInfo.urlKey + "\n";
                try
                {
                    if (agol.orgInfo.bingKey != "")
                    {
                        orgInfoString += "Bing Key: " + agol.orgInfo.bingKey + "\n";
                        Console.WriteLine(agol.orgInfo.bingKey.ToString());
                    }
                    else
                    {
                        orgInfoString += "Bing Key: No bing key" + "\n";
                    }
                }
                catch (NullReferenceException ex)
                {
                    orgInfoString += "Bing Key: No bing key" + "\n";
                    windowStatusLabel.Text = ex.ToString();
                }

                orgInfoLabel.Text = orgInfoString;
                
                string finalServiceList;
                finalServiceList = "";
                int i=0;

                foreach (var element in agol.orgServices.services)
                {
                    var linkLabel = new LinkLabel();
                    linkLabel.Text = element.name + "\n";
                    linkLabel.Links.Add(new LinkLabel.Link(i, element.url.Length, element.url));
                    i = linkLabel.Text.Length;
                    ServicesTab.Controls.Add(linkLabel);
                    linkLabel.LinkClicked += (s, z) =>
                        {
                            System.Diagnostics.Process.Start(z.Link.LinkData.ToString());
                        };
                }

                servicesLabel.Text = finalServiceList;

                windowStatusLabel.Text = "Finished!";
            }
            catch (NullReferenceException ex)
            {
                windowStatusLabel.Text = "Log in failed";
            }
        }
    }
}
