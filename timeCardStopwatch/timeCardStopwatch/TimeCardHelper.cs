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
            if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
<<<<<<< HEAD
                timers.SwitchActiveTimer("Premium Internation Desktop Extensions");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium Internation Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                timers.SwitchActiveTimer("Internation Desktop Extensions");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Internation Desktop Extensions";
=======
                StopAllStopWatches();
                stopwatchCasesPremiumInternationalDTEXT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium International Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                StopAllStopWatches();
                stopwatchCasesInternationalDTEXT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: International Desktop Extensions";
>>>>>>> origin/master
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                timers.SwitchActiveTimer("Premium Desktop Extensions");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                timers.SwitchActiveTimer("Domestic Desktop Extensions");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Domestic Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                timers.SwitchActiveTimer("Domestic Desktop");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Domestic Desktop";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
<<<<<<< HEAD
                timers.SwitchActiveTimer("Internation Desktop");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Internation Desktop";
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                timers.SwitchActiveTimer("Premium Internation Desktop");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium Internation Desktop";
=======
                StopAllStopWatches();
                stopwatchCasesInternationalDT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: International Desktop";
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                StopAllStopWatches();
                stopwatchCasesPremiumInternationalDT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium International Desktop";
>>>>>>> origin/master
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                timers.SwitchActiveTimer("Premium Desktop");
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium Desktop";
            }
        }

        private void collaborationButton_Click(object sender, EventArgs e)
        {
            timers.SwitchActiveTimer("Collaboration");
            timerToolStripStatusLabel.Text = "Currently Running Timer: Collaboration";
        }

        private void meetingButton_Click(object sender, EventArgs e)
        {
            timers.SwitchActiveTimer("Meetings");
            timerToolStripStatusLabel.Text = "Currently Running Timer: Meetings";
        }

        private void TimeCardHelper_Shown(object sender, EventArgs e)
        {
            caseComboBox.Items.Add("Desktop");
            caseComboBox.Items.Add("Desktop Extensions");
            caseComboBox.SelectedIndex = caseComboBox.FindString("Desktop");
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
<<<<<<< HEAD
            
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
            
=======
            tsCasesPremiumInternationalDTEXT = stopwatchCasesPremiumInternationalDTEXT.Elapsed;
            tsCasesInternationalDTEXT = stopwatchCasesInternationalDTEXT.Elapsed;
            tsCasesPremiumDTEXT = stopwatchCasesPremiumDomesticDTEXT.Elapsed;
            tsCasesDTEXT = stopwatchCasesDomesticDTEXT.Elapsed;
            tsCasesDT = stopwatchCasesDomesticDT.Elapsed;
            tsCasesPremiumDT = stopwatchCasesPremiumDomesticDT.Elapsed;
            tsCasesIntDT = stopwatchCasesInternationalDT.Elapsed;
            tsCasesPremiumIntDT = stopwatchCasesPremiumInternationalDT.Elapsed;

            TimeSpan tsMeetings = stopwatchMeetings.Elapsed;
            TimeSpan tsCollaboration = stopwatchCollaboration.Elapsed;

            TimeSpan totalSpanCases = tsCasesPremiumInternationalDTEXT + tsCasesInternationalDTEXT + tsCasesPremiumDTEXT + tsCasesDTEXT
                + tsCasesDT + tsCasesPremiumDT + tsCasesIntDT + tsCasesPremiumIntDT;

            TimeSpan totalTime = tsCasesPremiumInternationalDTEXT + tsCasesInternationalDTEXT + tsCasesPremiumDTEXT + tsCasesDTEXT
                + tsCasesDT + tsCasesPremiumDT + tsCasesIntDT + tsCasesPremiumIntDT + tsMeetings + tsCollaboration;

>>>>>>> origin/master
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
<<<<<<< HEAD
            timers.StopAllTimers();
            MessageBox.Show(timers.GetAllTimes());
=======
            StopAllStopWatches();
            MessageBox.Show("TE0352: " + meetingLabel.Text +
                "\nTE0353: " + collaborationLabel.Text +
                "\n C04550M0101: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesDTEXT.Hours, tsCasesDTEXT.Minutes, tsCasesDTEXT.Seconds) +
                "\n C04558M0101: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesPremiumInternationalDTEXT.Hours, tsCasesPremiumInternationalDTEXT.Minutes, tsCasesPremiumInternationalDTEXT.Seconds) +
                "\n C04552M0101: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesInternationalDTEXT.Hours, tsCasesInternationalDTEXT.Minutes, tsCasesInternationalDTEXT.Seconds) +
                "\n C04552M0101: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesPremiumDTEXT.Hours, tsCasesPremiumDTEXT.Minutes, tsCasesPremiumDTEXT.Seconds) +
                "\n C04550M0100: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesDT.Hours, tsCasesDT.Minutes, tsCasesDT.Seconds) +
                "\n C04552M0100: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesPremiumDT.Hours, tsCasesPremiumDT.Minutes, tsCasesPremiumDT.Seconds) +
                "\n C04551M0100: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesIntDT.Hours, tsCasesIntDT.Minutes, tsCasesIntDT.Seconds) +
                "\n C04558M0100: " + String.Format("{0:00}:{1:00}:{2:00}", tsCasesPremiumIntDT.Hours, tsCasesPremiumIntDT.Minutes, tsCasesPremiumIntDT.Seconds) +

                "\n\n Total Time: " + totalTimeLabel.Text);
>>>>>>> origin/master
        }

        private void lunchButton_Click(object sender, EventArgs e)
        {
            StopAllStopWatches();
            timerToolStripStatusLabel.Text = "On Lunch / break";
        }



    }
}
