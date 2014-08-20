using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace CreditQuest
{
    public partial class creidtConsumption : Form
    {
        public creidtConsumption()
        {
            InitializeComponent();
        }

        private void creditButton_Click(object sender, EventArgs e)
        {
            statusLabel.Text = "Working...";
            string username = usernameTextBoc.Text;
            string password = passwordTextBox.Text;
            AGOL agol = new AGOL("anohe_ess5", "GeogWorks3!");
            Console.WriteLine(agol.Username);
            Console.WriteLine(agol.URLKey);
            

            statusLabel.Text = "Complete!";
        }

        
    }
}
