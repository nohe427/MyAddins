using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace collatzConjucture
{
    public partial class collatzConjecture : Form
    {
        public collatzConjecture()
        {
            InitializeComponent();
        }

        int moves;

        private void runButton_Click(object sender, EventArgs e)
        {
            moves = 0;
            int numberEntered = 1;
            int.TryParse(numberTextBox.Text, out numberEntered);
            if (numberEntered < 2)
            {
                resultLabel.Text = "Enter a number greater than 1";
            }
            else
            {
                while (numberEntered != 1)
                {
                    if (IsOdd(numberEntered))
                    {
                        numberEntered = (numberEntered * 3) + 1;
                        Console.WriteLine(numberEntered.ToString());
                        moves += 1;
                    }
                    else
                    {
                        numberEntered/=2;
                        Console.WriteLine(numberEntered.ToString());
                        moves += 1;
                    }
                }
                Console.WriteLine(moves.ToString());
                resultLabel.Text = moves.ToString();
            }
        }
        
        public static bool IsOdd(int value)
        {
            return value % 2 != 0;
        }
    }
}
