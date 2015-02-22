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

        PictureBox selectedSquare;
        Image emptyImage;
        bool selectionMade;

        private void Form1_Shown(object sender, EventArgs e)
        {
            PictureBox[] pictures = new PictureBox[72];
            int x = 50;
            int y = 50;
            int width = 50;
            int height = 50;
            for(int i = 0; i < 72; i++)
            {
                pictures[i] = new PictureBox();
                pictures[i].Name = i.ToString();
                Color colorToUse = (i % 2) == 0 ? Color.Black : Color.AntiqueWhite;
                pictures[i].BackColor = colorToUse;
                pictures[i].Location = new Point(x, y);
                pictures[i].Size = new Size(width, height);
                if ((i % 2) == 0  && i < 27)
                {
                    Image image = resizeImage(new Bitmap(testbox.Properties.Resources._2000px_Disc_Plain_red_svg), new Size(25, 25));
                    pictures[i].Image = image;
                    pictures[i].SizeMode = PictureBoxSizeMode.CenterImage;
                }
                else if ((i % 2) == 0 && i > 44)
                {
                    Image image = resizeImage(new Bitmap(testbox.Properties.Resources.grayCircle), new Size(25, 25));
                    pictures[i].Image = image;
                    pictures[i].SizeMode = PictureBoxSizeMode.CenterImage;
                }
                this.Controls.Add(pictures[i]);
                x = x + width;
                if (x == 500)
                {
                    y = y + height;
                    x = 50;
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
            if (box.Image != null)
            {
                selectedSquare = box;
                selectionMade = true;
            }
            else if(selectionMade == true && box.Image == null)
            {
                emptyImage = box.Image;
                box.Image = selectedSquare.Image;
                selectedSquare.Image = emptyImage;
                box.SizeMode = PictureBoxSizeMode.CenterImage;
                selectionMade = false;
            }
        }

        public static Image resizeImage(Image imgToResize, Size size)
        {
            return (Image)(new Bitmap(imgToResize, size));
        }

    }
}
