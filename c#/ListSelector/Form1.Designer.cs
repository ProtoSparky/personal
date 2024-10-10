namespace ListSelector
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.DeviceDropdown = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.DeviceSaveBTN = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // DeviceDropdown
            // 
            this.DeviceDropdown.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.DeviceDropdown.FormattingEnabled = true;
            this.DeviceDropdown.Location = new System.Drawing.Point(36, 178);
            this.DeviceDropdown.Name = "DeviceDropdown";
            this.DeviceDropdown.Size = new System.Drawing.Size(242, 21);
            this.DeviceDropdown.TabIndex = 1;
            this.DeviceDropdown.DropDownClosed += new System.EventHandler(this.DeviceDropdown_DropDownClosed);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(33, 67);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(245, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Choose the secondary audio device for CtrlVolume";
            // 
            // DeviceSaveBTN
            // 
            this.DeviceSaveBTN.Cursor = System.Windows.Forms.Cursors.Default;
            this.DeviceSaveBTN.Enabled = false;
            this.DeviceSaveBTN.Location = new System.Drawing.Point(116, 246);
            this.DeviceSaveBTN.Name = "DeviceSaveBTN";
            this.DeviceSaveBTN.Size = new System.Drawing.Size(75, 23);
            this.DeviceSaveBTN.TabIndex = 3;
            this.DeviceSaveBTN.Text = "Save";
            this.DeviceSaveBTN.UseVisualStyleBackColor = true;
            this.DeviceSaveBTN.Click += new System.EventHandler(this.SaveDevice);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(339, 341);
            this.Controls.Add(this.DeviceSaveBTN);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.DeviceDropdown);
            this.Name = "Form1";
            this.Text = "CtrlVolume Setup";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.ComboBox DeviceDropdown;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button DeviceSaveBTN;
    }
}

