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

        Stopwatch stopwatchCollaboration = new Stopwatch();
        Stopwatch stopwatchMeetings = new Stopwatch();
        Stopwatch stopwatchCasesDomesticDT = new Stopwatch();
        Stopwatch stopwatchCasesInternationalDT = new Stopwatch();
        Stopwatch stopwatchCasesPremiumDomesticDT = new Stopwatch();
        Stopwatch stopwatchCasesPremiumInternationalDT = new Stopwatch();
        Stopwatch stopwatchCasesDomesticDTEXT = new Stopwatch();
        Stopwatch stopwatchCasesInternationalDTEXT = new Stopwatch();
        Stopwatch stopwatchCasesPremiumDomesticDTEXT = new Stopwatch();
        Stopwatch stopwatchCasesPremiumInternationalDTEXT = new Stopwatch();

        TimeSpan tsCasesPremiumInternationalDTEXT;
        TimeSpan tsCasesInternationalDTEXT;
        TimeSpan tsCasesPremiumDTEXT;
        TimeSpan tsCasesDTEXT;
        TimeSpan tsCasesDT;
        TimeSpan tsCasesPremiumDT;
        TimeSpan tsCasesIntDT;
        TimeSpan tsCasesPremiumIntDT;

        private void StopAllStopWatches()
        {
            stopwatchCollaboration.Stop();
            stopwatchMeetings.Stop();
            stopwatchCasesDomesticDT.Stop();
            stopwatchCasesDomesticDTEXT.Stop();
            stopwatchCasesInternationalDT.Stop();
            stopwatchCasesInternationalDTEXT.Stop();
            stopwatchCasesPremiumDomesticDT.Stop();
            stopwatchCasesPremiumDomesticDTEXT.Stop();
            stopwatchCasesPremiumInternationalDT.Stop();
            stopwatchCasesPremiumInternationalDTEXT.Stop();
        }

        private void caseButton_Click(object sender, EventArgs e)
        {
            if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                StopAllStopWatches();
                stopwatchCasesPremiumInternationalDTEXT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium International Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                StopAllStopWatches();
                stopwatchCasesInternationalDTEXT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: International Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                StopAllStopWatches();
                stopwatchCasesPremiumDomesticDTEXT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop Extensions")
            {
                StopAllStopWatches();
                stopwatchCasesDomesticDTEXT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Domestic Desktop Extensions";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                StopAllStopWatches();
                stopwatchCasesDomesticDT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Domestic Desktop";
            }
            else if (premiumCheckBox.Checked == false && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                StopAllStopWatches();
                stopwatchCasesInternationalDT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: International Desktop";
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == true && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                StopAllStopWatches();
                stopwatchCasesPremiumInternationalDT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium International Desktop";
            }
            else if (premiumCheckBox.Checked == true && internationalCheckBox.Checked == false && caseComboBox.SelectedItem.ToString() == "Desktop")
            {
                StopAllStopWatches();
                stopwatchCasesPremiumDomesticDT.Start();
                timerToolStripStatusLabel.Text = "Currently Running Timer: Premium Desktop";
            }
        }

        private void collaborationButton_Click(object sender, EventArgs e)
        {
            StopAllStopWatches();
            stopwatchCollaboration.Start();
            timerToolStripStatusLabel.Text = "Currently Running Timer: Collaboration";
        }

        private void meetingButton_Click(object sender, EventArgs e)
        {
            StopAllStopWatches();
            stopwatchMeetings.Start();
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
        }

        private void lunchButton_Click(object sender, EventArgs e)
        {
            StopAllStopWatches();
            timerToolStripStatusLabel.Text = "On Lunch / break";
        }



    }
}
