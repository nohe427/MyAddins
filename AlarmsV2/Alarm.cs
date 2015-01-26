using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;

namespace Alarms
{
    [Serializable()]
    public class Alarm
    {
        //Fields
        private string _alarmCategory;
        private DateTime _alarmTime;
        private bool _due;
        private bool _enabled;
        public string[] AlarmCategories = { "Personal", "Business" };

        //Properties
        public string AlarmCategory
        {
            get { return _alarmCategory; }
            set { _alarmCategory = value; }
        }

        public DateTime AlarmTime
        {
            get { return _alarmTime; }
            set { _alarmTime = value; }
        }

        public bool Due
        {
            get { return _due; }
            set { _due = value; }
        }

        public bool Enabled
        {
            get { return _enabled; }
            set { _enabled = value; }
        }

        //Methods
        public override string ToString()
        {
            return this._alarmTime.ToLongTimeString() + " - " + (this._enabled ? "Enabled" : "Disabled");
        }
    }
}
