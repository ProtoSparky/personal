﻿using System;
using System.Windows.Forms;

namespace ListSelector
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {

            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            bool variable = true;
            if (variable)
            {
                Application.Run(new Form1());
            }
            else
            {
                Console.WriteLine("Uwu");
            }

            /*
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());*/
        }
    }
}
