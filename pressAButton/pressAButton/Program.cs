using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Automation;
using System.Threading;
using System.Diagnostics;

namespace pressAButton
{
    class Program
    {

        
        
        static void Main(string[] args)
        {
            AutomationElement aeDesktop = AutomationElement.RootElement;
            AutomationElement aeTimeCard;

            do
            {
                Console.WriteLine("Looking for time card thing");

                aeTimeCard = aeDesktop.FindFirst(TreeScope.Children, new PropertyCondition(AutomationElement.NameProperty, "Time Card Helper"));
                Thread.Sleep(1000);
            } while (aeTimeCard == null);

            PropertyCondition prop1 = new PropertyCondition(AutomationElement.AutomationIdProperty, "caseButton");
            AutomationElement aeButton = aeTimeCard.FindFirst(TreeScope.Descendants, prop1);

            InvokePattern btnClick = aeButton.GetCurrentPattern(InvokePattern.Pattern) as InvokePattern;
            btnClick.Invoke();
        }
    }
}
