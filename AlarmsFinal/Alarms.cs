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
    public class Alarms
    {
        //Fields
        private List<Alarm> _alarms = new List<Alarm>();

        public List<Alarm> GetAlarms()
        {
            return _alarms;
        }

        //Method to add the alarm to the _alarms list.
        public void Add(Alarm alarm)
        {
            _alarms.Add(alarm);
        }

        //Method to delete the selected alarm from the list.
        public void DeleteAlarmFromList(int i)
        {
            _alarms.RemoveAt(i);
        }
        
        //Method to count the number of items in the _alarms list.
        public int Count()
        {
            int numberOfItems = 0;
            for (int i = 0; i < _alarms.Count; i++)
            {
                numberOfItems++;
            }
            return numberOfItems;
        }

        //Method to get an alarm from the _alarms list.
        public string GetAlarm(int index)
        {
            string item = "";
            for (int i = 0; i < _alarms.Count; i++)
            {
                item = _alarms[index].AlarmTime.ToLongTimeString();
            }
            return item;
        }

        //Method to get the alarm category.
        public string GetAlarmCategory(int index)
        {
            string category = "";
            for (int i = 0; i < _alarms.Count; i++)
            {
                category = _alarms[index].AlarmCategory;
            }
            return category;
        }

        //Overload method to get the alarm category by providing the alarm time.
        public string GetAlarmCategory(DateTime alarmTime)
        {
            string category = "";
            for (int i = 0; i < _alarms.Count; i++)
            {
                if (_alarms[i].AlarmTime == alarmTime)
                {
                    category = _alarms[i].AlarmCategory;
                }
            }
            return category;
        }

        //Method to get the alarm enabled status.
        public bool GetEnabledStatus(int index)
        {
            bool isEnabled = false;
            for (int i = 0; i < _alarms.Count; i++)
            {
                isEnabled = _alarms[index].Enabled;
            }
            return isEnabled;
        }

        //Method to get the alarm that's due.
        public DateTime GetNextDue(DateTime time)
        {
        	DateTime alarmDue = DateTime.Now.AddMinutes(1);
        	DateTime previousTime = DateTime.Now.AddMinutes(-2);
            //Foreach loop to search the _alarmsList times.
            foreach (Alarm items in _alarms)
            {
                if (items.Enabled == true)
                {
                	if (previousTime < items.AlarmTime)
                	{
                		previousTime = items.AlarmTime;
                    	alarmDue = items.AlarmTime;	
                	}
                }
            }
            return alarmDue;
        }

        //Method for searching the alarm list for a duplicate alarm.
        public bool Search(DateTime targetAlarm)
        {
            bool alarmExists = false;
            for (int i = 0; i < _alarms.Count; i++)
            {
                if (_alarms[i].AlarmTime == targetAlarm)
                {
                    alarmExists = true;
                }
            }
            return alarmExists;
        }

        public void SnoozeAlarm(int index)
        {
        }

        //Method to load the alarms from the file data.
        public void LoadAlarmsFromFile(string fileName)
        {
        	using(FileStream stream = File.Open(fileName, FileMode.Open))
        	{
            BinaryFormatter bin = new BinaryFormatter();
            _alarms = (List<Alarm>)bin.Deserialize(stream);
        	}
            //stream.Close();
        }

        //Method to save the file data.
        public void SaveAlarmsToFile(string fileName)
        {
        	using (FileStream stream = File.Open(fileName, FileMode.Create, FileAccess.ReadWrite))
        	{
            BinaryFormatter bin = new BinaryFormatter();
            bin.Serialize(stream, _alarms);
        	}
            //stream.Close();
        }

        //Test method used to see all the alarms in the list.
        public void GetAlarmsList()
        {
            foreach (Alarm items in _alarms)
            {
                Console.WriteLine(items.AlarmTime.ToLongTimeString() + " - " + (items.Enabled ? "Enabled" : "Disabled"));
            }
        }
    }
}