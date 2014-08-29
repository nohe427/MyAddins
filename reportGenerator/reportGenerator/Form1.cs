using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace reportGenerator
{
    public partial class Form1 : Form
    {
        string username;
        string password;
        string token;

        public Form1()
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
            }
        }
    }
}
