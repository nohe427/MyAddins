namespace andrewWang
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
            this.axMapControl1 = new ESRI.ArcGIS.Controls.AxMapControl();
            this.label1 = new System.Windows.Forms.Label();
            this.mapsComboBox = new System.Windows.Forms.ComboBox();
            this.loadMXDOCBbutton = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.layersListBox = new System.Windows.Forms.ListBox();
            this.fieldListBox = new System.Windows.Forms.ListBox();
            ((System.ComponentModel.ISupportInitialize)(this.axMapControl1)).BeginInit();
            this.SuspendLayout();
            // 
            // axMapControl1
            // 
            this.axMapControl1.Location = new System.Drawing.Point(491, 12);
            this.axMapControl1.Name = "axMapControl1";
            this.axMapControl1.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("axMapControl1.OcxState")));
            this.axMapControl1.Size = new System.Drawing.Size(367, 531);
            this.axMapControl1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 40);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "label1";
            // 
            // mapsComboBox
            // 
            this.mapsComboBox.FormattingEnabled = true;
            this.mapsComboBox.Location = new System.Drawing.Point(16, 66);
            this.mapsComboBox.Name = "mapsComboBox";
            this.mapsComboBox.Size = new System.Drawing.Size(180, 21);
            this.mapsComboBox.TabIndex = 2;
            this.mapsComboBox.SelectedIndexChanged += new System.EventHandler(this.mapsComboBox_SelectedIndexChanged);
            // 
            // loadMXDOCBbutton
            // 
            this.loadMXDOCBbutton.Location = new System.Drawing.Point(375, 35);
            this.loadMXDOCBbutton.Name = "loadMXDOCBbutton";
            this.loadMXDOCBbutton.Size = new System.Drawing.Size(75, 23);
            this.loadMXDOCBbutton.TabIndex = 3;
            this.loadMXDOCBbutton.Text = "Load MXD";
            this.loadMXDOCBbutton.UseVisualStyleBackColor = true;
            this.loadMXDOCBbutton.Click += new System.EventHandler(this.loadMXDOCBbutton_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(13, 131);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(35, 13);
            this.label2.TabIndex = 4;
            this.label2.Text = "label2";
            // 
            // layersListBox
            // 
            this.layersListBox.FormattingEnabled = true;
            this.layersListBox.Location = new System.Drawing.Point(16, 162);
            this.layersListBox.Name = "layersListBox";
            this.layersListBox.Size = new System.Drawing.Size(286, 134);
            this.layersListBox.TabIndex = 5;
            this.layersListBox.SelectedIndexChanged += new System.EventHandler(this.layersListBox_SelectedIndexChanged);
            // 
            // fieldListBox
            // 
            this.fieldListBox.FormattingEnabled = true;
            this.fieldListBox.Location = new System.Drawing.Point(16, 343);
            this.fieldListBox.Name = "fieldListBox";
            this.fieldListBox.Size = new System.Drawing.Size(286, 134);
            this.fieldListBox.TabIndex = 6;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(870, 555);
            this.Controls.Add(this.fieldListBox);
            this.Controls.Add(this.layersListBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.loadMXDOCBbutton);
            this.Controls.Add(this.mapsComboBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.axMapControl1);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.axMapControl1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private ESRI.ArcGIS.Controls.AxMapControl axMapControl1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox mapsComboBox;
        private System.Windows.Forms.Button loadMXDOCBbutton;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ListBox layersListBox;
        private System.Windows.Forms.ListBox fieldListBox;
    }
}

