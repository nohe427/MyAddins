using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PokemonApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        
        System.Reflection.Assembly myAssembly;

        private void loadButton_Click(object sender, EventArgs e)
        {
            myAssembly = this.GetType().Assembly;

            System.Resources.ResourceManager myManager = new 
   System.Resources.ResourceManager("PokemonApp.PokemonImages", 
   myAssembly);

            Image image = (System.Drawing.Image)PokemonApp.Properties.Resources.ResourceManager.GetObject("_001Bulbasaur_Dream");

            Monster bulbasaur = new Monster() { Name = "Bulbasaur", Image = image, Level = 1, Health = 100, MaxHealth = 200 };
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            label1.Text = "";
            typer(bulbasaur.Name, ref label1);
            pictureBox1.Image = bulbasaur.Image;
            pictureBox1.Refresh();
            progressBar1.Maximum = bulbasaur.MaxHealth;
            progressBar1.p
        }

        private void typer(string Phrase, ref Label labelText)
        {
            Stopwatch timer = new Stopwatch();
            foreach (char character in Phrase)
            {
                labelText.Text += character.ToString();
                System.Threading.Thread.Sleep(100);
                labelText.Refresh();
            }
        }
    }
}
