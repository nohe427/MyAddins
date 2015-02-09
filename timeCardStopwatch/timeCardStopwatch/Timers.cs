using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace timeCardStopwatch
{
    class Timers
    {
        private List<Timer> _timersActive = new List<Timer>();

        public List<Timer> TimersActive 
        {
            get
            {
                return _timersActive;
            }
        }

        public void AddTimer(string ChargeCode)
        {
            Timer timer = new Timer(ChargeCode);
            _timersActive.Add(timer);
        }

        public void StopAllTimers()
        {
            foreach (Timer timer in _timersActive)
            {
                timer.StopTime();
            }
        }

        public string GetAllTimes()
        {
            StringBuilder finalString = new StringBuilder();
            foreach (Timer timer in _timersActive)
            {
                finalString.Append(timer.Name+" ");
                finalString.Append(timer.RunningTimeString());
                finalString.Append("\n");
            }
            return finalString.ToString();
        }

        public void SwitchActiveTimer(string ChargeCode)
        {
            this.StopAllTimers();
            if (this._timersActive.Exists(x => x.Name == ChargeCode))
            {
                Timer timer = _timersActive.Find(x => x.Name == ChargeCode);
                timer.Stopwatch.Start();
            }
            else
            {
                this.AddTimer(ChargeCode);
            }
        }

        public TimeSpan AllTimes()
        {
            TimeSpan timespan = new TimeSpan();
            foreach (Timer timer in this._timersActive)
            {
                timespan += timer.Stopwatch.Elapsed;
            }
            return timespan;
        }

        public TimeSpan CaseTime()
        {
            TimeSpan totalSpanCases = new TimeSpan(0,0,0);
            foreach (Timer timer in this._timersActive)
            {
                if ((timer.Name != "Collaboration") && (timer.Name != "Meetings"))
                {
                    totalSpanCases += timer.Stopwatch.Elapsed;
                }
            }
            return totalSpanCases;
        }
    }
}
