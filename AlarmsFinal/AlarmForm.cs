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
    public partial class AlarmForm : Form
    {
        private Alarm _alarm;
        private Alarms _alarms;

        public Alarm Alarm
        {
            get { return _alarm; }
            set { _alarm = value; }
        }

        public Alarms Alarms
        {
            get { return _alarms; }
            set { _alarms = value; }
        }

        public AlarmForm()
        {
            InitializeComponent();
        }

        private void AlarmForm_Shown(object sender, EventArgs e)
        {
            //Setting the minimum and maximum values for the hour and minute boxes.
            hourNumericUpDown.Minimum = 1;
            hourNumericUpDown.Maximum = 24;
            minuteNumericUpDown.Maximum = 60;
        }

        private void okButton_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.OK;

            //Getting the hour and minute values from the up/down boxes.
            DateTime rightNow = DateTime.Now;
            int hour = Convert.ToInt32(hourNumericUpDown.Value);
            int minutes = Convert.ToInt32(minuteNumericUpDown.Value);
            
            //Using the hour and minute values for DateTime.
            DateTime value = new DateTime(rightNow.Year, rightNow.Month, rightNow.Day, hour, minutes, 0);

            //Getting the alarm category if selected.
            string category = "";
            if (categoryComboBox.SelectedIndex > -1)
            {
                category = categoryComboBox.SelectedItem.ToString();
            }
            else
                categoryComboBox.Text = "Personal";

            //Checking to see if the alarm is enabled.
            bool isEnabled = false;
            if (enabledCheckBox.Checked)
                isEnabled = true;

            //Creating the alarm object to be added to the list.
            _alarm = new Alarm()
            {
                AlarmCategory = category,
                AlarmTime = value,
                Enabled = isEnabled
            };
        }

        //This is used to populate the form if the user is editing an existing alarm.
        public AlarmForm(int hour, int minutes, string category, bool isEnabled)
        {
            //Loading the form with all the fields.
            InitializeComponent();

            //Setting the label showing that this an existing alarm to be edited.
            errorLabel.ForeColor = Color.Red;
            errorLabel.Text = "Existing Alarm";

            //Loading all of the data into the form.
            hourNumericUpDown.Value = hour;
            minuteNumericUpDown.Value = minutes;
            categoryComboBox.Text = category;
            if (isEnabled == true)
            {
                enabledCheckBox.Checked = true;
            }
            else
                enabledCheckBox.Checked = false;
        }

        private void cancelButton_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
        }
    }
}
