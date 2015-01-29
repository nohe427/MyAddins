using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace whatDidIDoToday
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            
        }

        Stopwatch stopwatchCollaboration = new Stopwatch();
        Stopwatch stopwatchMeetings = new Stopwatch();
        Stopwatch stopwatchCasesDomestic = new Stopwatch();

        private void button1_Click(object sender, EventArgs e)
        {
            stopwatchCollaboration.Start();
            stopwatchMeetings.Stop();
            stopwatchCasesDomestic.Stop();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            stopwatchCasesDomestic.Start();
            stopwatchMeetings.Stop();
            stopwatchCollaboration.Stop();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            TimeSpan tsCollaboration = stopwatchCollaboration.Elapsed;
            string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
            tsCollaboration.Hours, tsCollaboration.Minutes, tsCollaboration.Seconds,
            tsCollaboration.Milliseconds / 10);
            collaborationLabel.Text = elapsedTime;
            TimeSpan tsCasesDomestic = stopwatchCasesDomestic.Elapsed;
            caseDomesticLabel.Text = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
            tsCasesDomestic.Hours, tsCasesDomestic.Minutes, tsCasesDomestic.Seconds,
            tsCasesDomestic.Milliseconds / 10);
            TimeSpan tsMeetings = stopwatchMeetings.Elapsed;
            meetingsLabel.Text = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
            tsMeetings.Hours, tsMeetings.Minutes, tsMeetings.Seconds,
            tsMeetings.Milliseconds / 10);
            TimeSpan totalTime = tsCasesDomestic + tsCollaboration + tsMeetings;
            totalTimeLabel.Text = String.Format("{0:00}:{1:00}:{2:00}.{3:00}",
            totalTime.Hours, totalTime.Minutes, totalTime.Seconds,
            totalTime.Milliseconds / 10);
        }

        private void Form1_Shown(object sender, EventArgs e)
        {

        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            stopwatchCasesDomestic.Stop();
            stopwatchMeetings.Stop();
            stopwatchCollaboration.Stop();
            MessageBox.Show(String.Format(" TE0352 : {0}\n C04550M0100: {1}\n TE0353: {2}\n Total Time: {3}", meetingsLabel.Text, caseDomesticLabel.Text, collaborationLabel.Text, totalTimeLabel.Text));
        }

        private void meetingButton_Click(object sender, EventArgs e)
        {
            stopwatchMeetings.Start();
            stopwatchCollaboration.Stop();
            stopwatchCasesDomestic.Stop();
        }
    }
}
