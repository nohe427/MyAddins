using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics;

namespace timeCardStopwatch
{
    public partial class TimeCardHelper : Form
    {
        public TimeCardHelper()
        {
            InitializeComponent();
        }

        Timers timers = new Timers();
        TimeSpan totalTime = new TimeSpan();
        TimeSpan tsMeetings = new TimeSpan();
        TimeSpan tsCollaboration = new TimeSpan();
        TimeSpan totalSpanCases = new TimeSpan(0,0,0);

        private void StopAllStopWatches()
        {
            timers.StopAllTimers();
        }

        private void caseButton_Click(object sender, EventArgs e)
        {
            string part1 = "";
            string part2 = "";
            if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == true)
            {
                part1 = "C04573";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == true)
            {
                part1 = "C04571";
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == false)
            {
                part1 = "C04572";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == false)
            {
                part1 = "C04570";
            }

            if (caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                part2 = "M0101";
            }
            else if (caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                part2 = "M0100";
            }
            else if (caseComboBox.SelectedItem.ToString() == "ArcGIS Online")
            {
                part2 = "M0125";
            }
            else if (caseComboBox.SelectedItem.ToString() == "Raster")
            {
                part2 = "M0114";
            }
            else if (caseComboBox.SelectedItem.ToString() == "Mobile")
            {
                part2 = "M0104";
            }
            else if (caseComboBox.SelectedItem.ToString() == "SDK")
            {
                part2 = "M0116";
            }
            else if (caseComboBox.SelectedItem.ToString() == "ArcGIS Server")
            {
                part2 = "M0121";
            }
            else if (caseComboBox.SelectedItem.ToString() == "Implementation")
            {
                part2 = "M0133";
            }
            else if (caseComboBox.SelectedItem.ToString() == "Geodata")
            {
                part2 = "M0112";
            }
            string timerCalled = part1 + part2;
            timers.SwitchActiveTimer(timerCalled);
            timerToolStripStatusLabel.Text = "Currently Running Timer: " + timerCalled;
        }

        private void collaborationButton_Click(object sender, EventArgs e)
        {
            timers.SwitchActiveTimer("TE0353");
            timerToolStripStatusLabel.Text = "Currently Running Timer: Collaboration";
        }

        private void meetingButton_Click(object sender, EventArgs e)
        {
            timers.SwitchActiveTimer("TE0351");
            timerToolStripStatusLabel.Text = "Currently Running Timer: Meetings";
        }

        private void TimeCardHelper_Shown(object sender, EventArgs e)
        {
            caseComboBox.Items.Add("Desktop");
            caseComboBox.Items.Add("Desktop Extensions");
            caseComboBox.Items.Add("ArcGIS Online");
            caseComboBox.Items.Add("Raster");
            caseComboBox.Items.Add("Mobile");
            caseComboBox.Items.Add("SDK");
            caseComboBox.Items.Add("ArcGIS Server");
            caseComboBox.Items.Add("Implementation");
            caseComboBox.Items.Add("Geodata");
            caseComboBox.SelectedIndex = caseComboBox.FindString("Desktop");
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

            if(timers.TimersActive.Exists(x => x.Name == "Meetings"))
            {
                tsMeetings = timers.TimersActive.Find(x => x.Name == "Meetings").Stopwatch.Elapsed;
            }
            if (timers.TimersActive.Exists(x => x.Name == "Collaboration"))
            {
                tsCollaboration = timers.TimersActive.Find(x => x.Name == "Collaboration").Stopwatch.Elapsed;
            }

            totalSpanCases = timers.CaseTime();

            totalTime = timers.AllTimes();

            caseLabel.Text = String.Format("{0:00}:{1:00}:{2:00}",
            totalSpanCases.Hours, totalSpanCases.Minutes, totalSpanCases.Seconds);

            meetingLabel.Text = String.Format("{0:00}:{1:00}:{2:00}",
            tsMeetings.Hours, tsMeetings.Minutes, tsMeetings.Seconds);

            collaborationLabel.Text = String.Format("{0:00}:{1:00}:{2:00}",
            tsCollaboration.Hours, tsCollaboration.Minutes, tsCollaboration.Seconds);

            totalTimeLabel.Text = String.Format("{0:00}:{1:00}:{2:00}",
            totalTime.Hours, totalTime.Minutes, totalTime.Seconds);

            if (totalTime.Hours == 8)
            {
                totalTimeLabel.BackColor = System.Drawing.Color.Green;
                totalTimeLabel.ForeColor = System.Drawing.Color.White;
            }
        }

        private void TimeCardHelper_FormClosing(object sender, FormClosingEventArgs e)
        {

            timers.StopAllTimers();
            MessageBox.Show(timers.GetAllTimes());
        }

        private void lunchButton_Click(object sender, EventArgs e)
        {
            StopAllStopWatches();
            timerToolStripStatusLabel.Text = "On Lunch / break";
        }



    }
}
