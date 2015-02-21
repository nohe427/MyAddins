using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace testbox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Shown(object sender, EventArgs e)
        {
            PictureBox[] pictures = new PictureBox[64];
            int x = 50;
            int y = 50;
            int width = 50;
            int height = 50;
            for(int i = 0; i < 63; i++)
            {
                pictures[i] = new PictureBox();
                pictures[i].Name = i.ToString();
                Color colorToUse = (i % 2) == 0 ? Color.Black : Color.AntiqueWhite;
                pictures[i].BackColor = colorToUse;
                pictures[i].Location = new Point(x, y);
                pictures[i].Size = new Size(width, height);
                this.Controls.Add(pictures[i]);
                x = x + width;
                if (x == 500)
                {
                    y = y + height;
                    x = 50;
                }
                if ((i % 2) == 0)
                {
                    PictureBox box = new PictureBox();
                    Graphics ellipse = box;
                    
                }
            }
            foreach (PictureBox box in this.Controls.OfType<PictureBox>())
            {
                box.Click += new System.EventHandler(this.myEventHandler);
            }
        }

        public void myEventHandler(object sender, EventArgs e)
        {
            PictureBox box = sender as PictureBox;
            MessageBox.Show(box.Name.ToString());
        }
    }
}
