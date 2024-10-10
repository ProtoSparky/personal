using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Clock_app
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            clock.Text = DateTime.Now.ToString("HH:mm:ss"); // set the time to current time instead of waiting a second for the timer tick to pipulate it
            timer1.Interval = 1000;
            timer1.Tick += timer1_Tick;
            timer1.Start();
        }
        private void timer1_Tick(object sender, EventArgs e)
        {
            int seconds = Convert.ToInt32(DateTime.Now.ToString("ss"));
            double red = seconds * 4.3220338983;
            double blue = 255 / 59 ^ 2 * seconds ^ 2;
            double green = 127.5 * Math.Sin(Math.PI / 59 * seconds - Math.PI / 2) + 127.5; 
            clock.Text = DateTime.Now.ToString("HH:mm:ss");
            clock.BackColor = Color.FromArgb(Convert.ToInt32(red), Convert.ToInt32(green), Convert.ToInt32(blue), 0);

            checkedListBox1.Items.Add(seconds);
            Console.WriteLine(checkedListBox1.CheckedItems.IndexOf(0));
        }
    }
}
