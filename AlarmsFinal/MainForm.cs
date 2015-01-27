using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;

namespace Alarms
{
    [Serializable()]
    public partial class MainForm : Form
    {
        private Alarms _alarms = new Alarms();
        string dataPath = Application.StartupPath + @"\data\Alarm Data.data";    //Setting the data file path.

        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Shown(object sender, EventArgs e)
        {
            //Enabling the timer for the current time.
            alarmTimer.Enabled = true;
            timeLabel.Text = DateTime.Now.ToLongTimeString();

            //Loading any data that might be saved.
            using (StreamWriter w = File.AppendText(dataPath));
            _alarms.LoadAlarmsFromFile(dataPath);
            refreshAlarmsList();
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            //Showing the AlarmForm dialog box.
            AlarmForm alarmForm = new AlarmForm();
            alarmForm.ShowDialog();

            if (alarmForm.DialogResult == DialogResult.OK)
            {
                bool alarmExists = _alarms.Search(alarmForm.Alarm.AlarmTime);
                //Checking to see if the alarm exists. If not it will be added to the form.
                if (alarmExists)
                {
                    MessageBox.Show("Sorry cannot add a duplicate alarm time.", this.Text, MessageBoxButtons.OK);

                    //Refreshing the alarms listbox.
                    refreshAlarmsList();
                }
                else
                {
                    //Adding the alarm object to the list.
                    _alarms.Add(alarmForm.Alarm);

                    //Saving the data.
                    _alarms.SaveAlarmsToFile(dataPath);

                    //Refreshing the alarms listbox.
                    refreshAlarmsList();
                }
            }
        }

        private void editButton_Click(object sender, EventArgs e)
        {
            //Making sure there is an alarm in the form to edit.
            if (alarmsListBox.SelectedIndex > -1)
            {
                //Getting the alarm time.
                string alarmTime = _alarms.GetAlarm(alarmsListBox.SelectedIndex);
                DateTime time = DateTime.Parse(alarmTime);
                int hour = int.Parse(time.ToString("HH"));
                int minutes = int.Parse(time.ToString("mm"));

                //Getting the alarm category.
                string category = _alarms.GetAlarmCategory(alarmsListBox.SelectedIndex);

                //Getting the alarm enabled status.
                bool enabled = _alarms.GetEnabledStatus(alarmsListBox.SelectedIndex);

                AlarmForm editAlarmForm = new AlarmForm(hour, minutes, category, enabled);
                editAlarmForm.ShowDialog();

                //Removing the alarm to be edited. This is so it won't think the edited alarm is a duplicate.
                _alarms.DeleteAlarmFromList(alarmsListBox.SelectedIndex);

                if (editAlarmForm.DialogResult == DialogResult.OK)
                {
                    bool alarmExists = _alarms.Search(editAlarmForm.Alarm.AlarmTime);
                    //Checking to see if the edited alarm already exists. If so removing it and the user will have to re-add the alarm.
                    if (alarmExists)
                    {
                        MessageBox.Show("Sorry, cannot edit an alarm to an already existing time. Please re-add your alarm.", this.Text, MessageBoxButtons.OK);

                        //Refreshing the alarms listbox.
                        refreshAlarmsList();
                    }
                    else
                    {
                        //Removing an re-adding the edited alarm to the _alarms list and the mainform listbox.
                        _alarms.Add(editAlarmForm.Alarm);
                        refreshAlarmsList();
                        _alarms.GetAlarmsList();    //Test method call to verify the edited alarms was added to the list. Can remove later.
                    }
                }
            }
            else
            {
                MessageBox.Show("No alarms selected for editing.", this.Text, MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {
            //Checking to make sure an alarm has been selected or the listbox is populated.
            if (alarmsListBox.SelectedIndex > -1)
            {
                if (MessageBox.Show("Delete " + _alarms.GetAlarm(alarmsListBox.SelectedIndex) + " alarm?", "Delete Alarm",
                MessageBoxButtons.OKCancel, MessageBoxIcon.Question) == DialogResult.OK)
                {
                    _alarms.DeleteAlarmFromList(alarmsListBox.SelectedIndex);    //Deleting the alarm from the list in Alarms.cs.
                    refreshAlarmsList();
                    _alarms.GetAlarmsList();    //Test method call to verify the alarm was removed from the list. Can remove later.
                }
            }
            else
            {
                MessageBox.Show("No alarms selected to delete.", this.Text, MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void alarmsListBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            //Saving the alarm list data.
            _alarms.SaveAlarmsToFile(dataPath);
        }

        private void alarmTimer_Tick(object sender, EventArgs e)
        {
            //Getting the time and changing the text on the MainForm to reflect the current time.
            DateTime timeNow = DateTime.Now;
            timeLabel.Text = timeNow.ToLongTimeString();

            //Calling the method to check the alarms list times.
            DateTime alarms = _alarms.GetNextDue(timeNow);
            
            //Checking to see if an alarm should be displaying.
            if (timeNow.Hour == alarms.Hour && timeNow.Minute == alarms.Minute && timeNow.Second == alarms.Second)
            {
                //alarmTimer.Enabled = true;
                MessageBox.Show(alarms.ToString() + "\n" + _alarms.GetAlarmCategory(alarms), "Alarm", MessageBoxButtons.OK);
            }        
        }

        private void refreshAlarmsList()
        {
            //Un-binding and re-binding the listbox datasource. This is so the listbox can refresh itself while referencing the _alarms list.
            alarmsListBox.DataSource = null;
            alarmsListBox.DataSource = _alarms.GetAlarms();
            alarmsListBox.Refresh();
        }
    }
}

//Personal additions.
//Work on a snooze function. Say if the user clicks ok after the alarm goes off the alarm snoozes for 10 minutes. 
//If cancel button is pressed then the alarm is removed.