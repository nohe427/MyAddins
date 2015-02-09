using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace timeCardStopwatch
{
    class Timer
    {
        private string _name;
        private Stopwatch _stopwatch;

        public string Name
        {
            get
            {
                return _name;
            }
            set
            {
                _name = value;
            }
        }

        public Stopwatch Stopwatch
        {
            get
            {
                return _stopwatch;
            }
        }

        public Timer(string chargeCode)
        {
            _name = chargeCode;
            _stopwatch = new Stopwatch();
            _stopwatch.Start();
        }

        public void StopTime()
        {
            _stopwatch.Stop();
        }

        public string RunningTimeString()
        {
            string totalTime = String.Format("{0:00}:{1:00}:{2:00}", _stopwatch.Elapsed.Hours, _stopwatch.Elapsed.Minutes, _stopwatch.Elapsed.Seconds);
            return totalTime;
        }

    }
}
