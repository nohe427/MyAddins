namespace FlipLine
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.dataViewerMapControl = new ESRI.ArcGIS.Controls.AxMapControl();
            this.default_button = new System.Windows.Forms.Button();
            this.load_button = new System.Windows.Forms.Button();
            this.oidLabel = new System.Windows.Forms.Label();
            this.previous_button = new System.Windows.Forms.Button();
            this.next_button = new System.Windows.Forms.Button();
            this.objectIDListBox = new System.Windows.Forms.ListBox();
            this.flip_button = new System.Windows.Forms.Button();
            this.exit_button = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataViewerMapControl)).BeginInit();
            this.SuspendLayout();
            // 
            // dataViewerMapControl
            // 
            this.dataViewerMapControl.Location = new System.Drawing.Point(268, 12);
            this.dataViewerMapControl.Name = "dataViewerMapControl";
            this.dataViewerMapControl.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("dataViewerMapControl.OcxState")));
            this.dataViewerMapControl.Size = new System.Drawing.Size(856, 583);
            this.dataViewerMapControl.TabIndex = 0;
            // 
            // default_button
            // 
            this.default_button.Location = new System.Drawing.Point(15, 12);
            this.default_button.Name = "default_button";
            this.default_button.Size = new System.Drawing.Size(247, 23);
            this.default_button.TabIndex = 1;
            this.default_button.Text = "Load Default Data";
            this.default_button.UseVisualStyleBackColor = true;
            this.default_button.Click += new System.EventHandler(this.default_button_Click);
            // 
            // load_button
            // 
            this.load_button.Location = new System.Drawing.Point(15, 41);
            this.load_button.Name = "load_button";
            this.load_button.Size = new System.Drawing.Size(247, 23);
            this.load_button.TabIndex = 2;
            this.load_button.Text = "Load My Data";
            this.load_button.UseVisualStyleBackColor = true;
            this.load_button.Click += new System.EventHandler(this.load_button_Click);
            // 
            // oidLabel
            // 
            this.oidLabel.AutoSize = true;
            this.oidLabel.Location = new System.Drawing.Point(12, 100);
            this.oidLabel.Name = "oidLabel";
            this.oidLabel.Size = new System.Drawing.Size(59, 13);
            this.oidLabel.TabIndex = 3;
            this.oidLabel.Text = "Object IDS";
            // 
            // previous_button
            // 
            this.previous_button.Location = new System.Drawing.Point(12, 539);
            this.previous_button.Name = "previous_button";
            this.previous_button.Size = new System.Drawing.Size(120, 23);
            this.previous_button.TabIndex = 4;
            this.previous_button.Text = "Previous";
            this.previous_button.UseVisualStyleBackColor = true;
            this.previous_button.Click += new System.EventHandler(this.previous_button_Click);
            // 
            // next_button
            // 
            this.next_button.Location = new System.Drawing.Point(142, 539);
            this.next_button.Name = "next_button";
            this.next_button.Size = new System.Drawing.Size(120, 23);
            this.next_button.TabIndex = 5;
            this.next_button.Text = "Next";
            this.next_button.UseVisualStyleBackColor = true;
            this.next_button.Click += new System.EventHandler(this.next_button_Click);
            // 
            // objectIDListBox
            // 
            this.objectIDListBox.FormattingEnabled = true;
            this.objectIDListBox.Location = new System.Drawing.Point(12, 125);
            this.objectIDListBox.Name = "objectIDListBox";
            this.objectIDListBox.Size = new System.Drawing.Size(250, 173);
            this.objectIDListBox.TabIndex = 6;
            this.objectIDListBox.SelectedIndexChanged += new System.EventHandler(this.objectIDListBox_SelectedIndexChanged);
            // 
            // flip_button
            // 
            this.flip_button.Location = new System.Drawing.Point(12, 304);
            this.flip_button.Name = "flip_button";
            this.flip_button.Size = new System.Drawing.Size(247, 23);
            this.flip_button.TabIndex = 7;
            this.flip_button.Text = "Flip";
            this.flip_button.UseVisualStyleBackColor = true;
            this.flip_button.Click += new System.EventHandler(this.flip_button_Click);
            // 
            // exit_button
            // 
            this.exit_button.Location = new System.Drawing.Point(142, 568);
            this.exit_button.Name = "exit_button";
            this.exit_button.Size = new System.Drawing.Size(120, 23);
            this.exit_button.TabIndex = 8;
            this.exit_button.Text = "Exit";
            this.exit_button.UseVisualStyleBackColor = true;
            this.exit_button.Click += new System.EventHandler(this.exit_button_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1136, 607);
            this.Controls.Add(this.exit_button);
            this.Controls.Add(this.flip_button);
            this.Controls.Add(this.objectIDListBox);
            this.Controls.Add(this.next_button);
            this.Controls.Add(this.previous_button);
            this.Controls.Add(this.oidLabel);
            this.Controls.Add(this.load_button);
            this.Controls.Add(this.default_button);
            this.Controls.Add(this.dataViewerMapControl);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dataViewerMapControl)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private ESRI.ArcGIS.Controls.AxMapControl dataViewerMapControl;
        private System.Windows.Forms.Button default_button;
        private System.Windows.Forms.Button load_button;
        private System.Windows.Forms.Label oidLabel;
        private System.Windows.Forms.Button previous_button;
        private System.Windows.Forms.Button next_button;
        private System.Windows.Forms.ListBox objectIDListBox;
        private System.Windows.Forms.Button flip_button;
        private System.Windows.Forms.Button exit_button;
    }
}

