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
            
        }
        
        public static bool IsOdd(int value)
        {
            return value % 2 != 0;
        }
    }
}
