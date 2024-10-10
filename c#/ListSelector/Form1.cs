using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ListSelector
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            List<string> AllAudioDevices = new List<string>(); 
            //populate array
            AllAudioDevices.Add("Device one");
            AllAudioDevices.Add("Device two");

            int DeviceAmount = AllAudioDevices.Count();
            for(int DevicePointer = 0; DevicePointer < DeviceAmount; DevicePointer++)
            {
                DeviceDropdown.Items.Add(AllAudioDevices[DevicePointer]);
            }

        }       

        private void DeviceDropdown_DropDownClosed(object sender, EventArgs e)
        {
            if(DeviceDropdown.SelectedIndex != -1)
            {
                //check if the user actually selected something before closing the box

                //Change save button from disabled to enabled
                DeviceSaveBTN.Enabled = true;
            }
        }


        private void SaveDevice(object sender, EventArgs e)
        {
            Console.WriteLine("Saving Device");
            Console.WriteLine(DeviceDropdown.SelectedItem);
            Close();

        }
    }
}
