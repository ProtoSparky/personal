namespace Clock_app
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
            this.components = new System.ComponentModel.Container();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.timer2 = new System.Windows.Forms.Timer(this.components);
            this.timer3 = new System.Windows.Forms.Timer(this.components);
            this.timer4 = new System.Windows.Forms.Timer(this.components);
            this.clock = new System.Windows.Forms.Label();
            this.list_box = new System.Windows.Forms.ListView();
            this.checkedListBox1 = new System.Windows.Forms.CheckedListBox();
            this.SuspendLayout();
            // 
            // clock
            // 
            this.clock.Anchor = System.Windows.Forms.AnchorStyles.None;
            this.clock.AutoSize = true;
            this.clock.Cursor = System.Windows.Forms.Cursors.No;
            this.clock.Font = new System.Drawing.Font("Microsoft Sans Serif", 100F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.clock.Location = new System.Drawing.Point(102, 139);
            this.clock.Name = "clock";
            this.clock.Size = new System.Drawing.Size(589, 153);
            this.clock.TabIndex = 0;
            this.clock.Text = "42:00:69";
            this.clock.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // list_box
            // 
            this.list_box.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.list_box.CheckBoxes = true;
            this.list_box.Cursor = System.Windows.Forms.Cursors.Default;
            this.list_box.HideSelection = false;
            this.list_box.Location = new System.Drawing.Point(12, 38);
            this.list_box.Name = "list_box";
            this.list_box.Size = new System.Drawing.Size(107, 374);
            this.list_box.TabIndex = 1;
            this.list_box.UseCompatibleStateImageBehavior = false;
            // 
            // checkedListBox1
            // 
            this.checkedListBox1.FormattingEnabled = true;
            this.checkedListBox1.Location = new System.Drawing.Point(677, 28);
            this.checkedListBox1.Name = "checkedListBox1";
            this.checkedListBox1.Size = new System.Drawing.Size(120, 94);
            this.checkedListBox1.TabIndex = 2;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.checkedListBox1);
            this.Controls.Add(this.list_box);
            this.Controls.Add(this.clock);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Timer timer2;
        private System.Windows.Forms.Timer timer3;
        private System.Windows.Forms.Timer timer4;
        private System.Windows.Forms.Label clock;
        private System.Windows.Forms.ListView list_box;
        private System.Windows.Forms.CheckedListBox checkedListBox1;
    }
}

