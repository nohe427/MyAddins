namespace reportGenerator
{
    partial class ReportGenerator
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
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.businessSummaryCheckBox = new System.Windows.Forms.CheckBox();
            this.census2010CheckBox = new System.Windows.Forms.CheckBox();
            this.dandiCheckBox = new System.Windows.Forms.CheckBox();
            this.usernameLabel = new System.Windows.Forms.Label();
            this.usernameTextBox = new System.Windows.Forms.TextBox();
            this.passwordLabel = new System.Windows.Forms.Label();
            this.passwordTextBox = new System.Windows.Forms.TextBox();
            this.logonButton = new System.Windows.Forms.Button();
            this.getReportsButton = new System.Windows.Forms.Button();
            this.zipCodeLabel = new System.Windows.Forms.Label();
            this.zipCodeTextBox = new System.Windows.Forms.TextBox();
            this.storageLocationLabel = new System.Windows.Forms.Label();
            this.storageLocationTextBox = new System.Windows.Forms.TextBox();
            this.statusStrip1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1});
            this.statusStrip1.Location = new System.Drawing.Point(0, 331);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(455, 22);
            this.statusStrip1.TabIndex = 0;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(35, 17);
            this.toolStripStatusLabel1.Text = "Idle...";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.businessSummaryCheckBox);
            this.groupBox1.Controls.Add(this.census2010CheckBox);
            this.groupBox1.Controls.Add(this.dandiCheckBox);
            this.groupBox1.Location = new System.Drawing.Point(12, 102);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(435, 161);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Reports";
            // 
            // businessSummaryCheckBox
            // 
            this.businessSummaryCheckBox.AutoSize = true;
            this.businessSummaryCheckBox.Location = new System.Drawing.Point(7, 67);
            this.businessSummaryCheckBox.Name = "businessSummaryCheckBox";
            this.businessSummaryCheckBox.Size = new System.Drawing.Size(114, 17);
            this.businessSummaryCheckBox.TabIndex = 2;
            this.businessSummaryCheckBox.Text = "Business Summary";
            this.businessSummaryCheckBox.UseVisualStyleBackColor = true;
            // 
            // census2010CheckBox
            // 
            this.census2010CheckBox.AutoSize = true;
            this.census2010CheckBox.Location = new System.Drawing.Point(7, 43);
            this.census2010CheckBox.Name = "census2010CheckBox";
            this.census2010CheckBox.Size = new System.Drawing.Size(114, 17);
            this.census2010CheckBox.TabIndex = 1;
            this.census2010CheckBox.Text = "Census 210 Profile";
            this.census2010CheckBox.UseVisualStyleBackColor = true;
            // 
            // dandiCheckBox
            // 
            this.dandiCheckBox.AutoSize = true;
            this.dandiCheckBox.Location = new System.Drawing.Point(7, 20);
            this.dandiCheckBox.Name = "dandiCheckBox";
            this.dandiCheckBox.Size = new System.Drawing.Size(180, 17);
            this.dandiCheckBox.TabIndex = 0;
            this.dandiCheckBox.Text = "Demographic and Income Profile";
            this.dandiCheckBox.UseVisualStyleBackColor = true;
            // 
            // usernameLabel
            // 
            this.usernameLabel.AutoSize = true;
            this.usernameLabel.Location = new System.Drawing.Point(12, 21);
            this.usernameLabel.Name = "usernameLabel";
            this.usernameLabel.Size = new System.Drawing.Size(58, 13);
            this.usernameLabel.TabIndex = 2;
            this.usernameLabel.Text = "Username:";
            // 
            // usernameTextBox
            // 
            this.usernameTextBox.Location = new System.Drawing.Point(76, 18);
            this.usernameTextBox.Name = "usernameTextBox";
            this.usernameTextBox.Size = new System.Drawing.Size(137, 20);
            this.usernameTextBox.TabIndex = 3;
            // 
            // passwordLabel
            // 
            this.passwordLabel.AutoSize = true;
            this.passwordLabel.Location = new System.Drawing.Point(248, 21);
            this.passwordLabel.Name = "passwordLabel";
            this.passwordLabel.Size = new System.Drawing.Size(56, 13);
            this.passwordLabel.TabIndex = 4;
            this.passwordLabel.Text = "Password:";
            // 
            // passwordTextBox
            // 
            this.passwordTextBox.Location = new System.Drawing.Point(310, 18);
            this.passwordTextBox.Name = "passwordTextBox";
            this.passwordTextBox.PasswordChar = '*';
            this.passwordTextBox.Size = new System.Drawing.Size(137, 20);
            this.passwordTextBox.TabIndex = 5;
            // 
            // logonButton
            // 
            this.logonButton.Location = new System.Drawing.Point(352, 61);
            this.logonButton.Name = "logonButton";
            this.logonButton.Size = new System.Drawing.Size(95, 23);
            this.logonButton.TabIndex = 6;
            this.logonButton.Text = "Log In to ArcGIS Online";
            this.logonButton.UseVisualStyleBackColor = true;
            this.logonButton.Click += new System.EventHandler(this.logonButton_Click);
            // 
            // getReportsButton
            // 
            this.getReportsButton.Location = new System.Drawing.Point(372, 297);
            this.getReportsButton.Name = "getReportsButton";
            this.getReportsButton.Size = new System.Drawing.Size(75, 23);
            this.getReportsButton.TabIndex = 7;
            this.getReportsButton.Text = "Get Reports";
            this.getReportsButton.UseVisualStyleBackColor = true;
            this.getReportsButton.Click += new System.EventHandler(this.getReportsButton_Click);
            // 
            // zipCodeLabel
            // 
            this.zipCodeLabel.AutoSize = true;
            this.zipCodeLabel.Location = new System.Drawing.Point(12, 274);
            this.zipCodeLabel.Name = "zipCodeLabel";
            this.zipCodeLabel.Size = new System.Drawing.Size(53, 13);
            this.zipCodeLabel.TabIndex = 8;
            this.zipCodeLabel.Text = "Zip Code:";
            // 
            // zipCodeTextBox
            // 
            this.zipCodeTextBox.Location = new System.Drawing.Point(71, 271);
            this.zipCodeTextBox.Name = "zipCodeTextBox";
            this.zipCodeTextBox.Size = new System.Drawing.Size(120, 20);
            this.zipCodeTextBox.TabIndex = 9;
            // 
            // storageLocationLabel
            // 
            this.storageLocationLabel.AutoSize = true;
            this.storageLocationLabel.Location = new System.Drawing.Point(197, 274);
            this.storageLocationLabel.Name = "storageLocationLabel";
            this.storageLocationLabel.Size = new System.Drawing.Size(88, 13);
            this.storageLocationLabel.TabIndex = 10;
            this.storageLocationLabel.Text = "Storage Location";
            // 
            // storageLocationTextBox
            // 
            this.storageLocationTextBox.Location = new System.Drawing.Point(291, 271);
            this.storageLocationTextBox.Name = "storageLocationTextBox";
            this.storageLocationTextBox.Size = new System.Drawing.Size(156, 20);
            this.storageLocationTextBox.TabIndex = 11;
            // 
            // ReportGenerator
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(455, 353);
            this.Controls.Add(this.storageLocationTextBox);
            this.Controls.Add(this.storageLocationLabel);
            this.Controls.Add(this.zipCodeTextBox);
            this.Controls.Add(this.zipCodeLabel);
            this.Controls.Add(this.getReportsButton);
            this.Controls.Add(this.logonButton);
            this.Controls.Add(this.passwordTextBox);
            this.Controls.Add(this.passwordLabel);
            this.Controls.Add(this.usernameTextBox);
            this.Controls.Add(this.usernameLabel);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.statusStrip1);
            this.Name = "ReportGenerator";
            this.Text = "Report Generator";
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label usernameLabel;
        private System.Windows.Forms.TextBox usernameTextBox;
        private System.Windows.Forms.Label passwordLabel;
        private System.Windows.Forms.TextBox passwordTextBox;
        private System.Windows.Forms.Button logonButton;
        private System.Windows.Forms.Button getReportsButton;
        private System.Windows.Forms.Label zipCodeLabel;
        private System.Windows.Forms.TextBox zipCodeTextBox;
        private System.Windows.Forms.Label storageLocationLabel;
        private System.Windows.Forms.TextBox storageLocationTextBox;
        private System.Windows.Forms.CheckBox businessSummaryCheckBox;
        private System.Windows.Forms.CheckBox census2010CheckBox;
        private System.Windows.Forms.CheckBox dandiCheckBox;
    }
}

