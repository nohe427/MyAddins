namespace timeCardStopwatch
{
    partial class TimeCardHelper
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(TimeCardHelper));
            this.premiumCheckBox = new System.Windows.Forms.CheckBox();
            this.internationalCheckBox = new System.Windows.Forms.CheckBox();
            this.caseComboBox = new System.Windows.Forms.ComboBox();
            this.caseButton = new System.Windows.Forms.Button();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.timerToolStripStatusLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.collaborationButton = new System.Windows.Forms.Button();
            this.meetingButton = new System.Windows.Forms.Button();
            this.caseLabel = new System.Windows.Forms.Label();
            this.collaborationLabel = new System.Windows.Forms.Label();
            this.meetingLabel = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.DescriptiveLabel = new System.Windows.Forms.Label();
            this.totalTimeLabel = new System.Windows.Forms.Label();
            this.lunchButton = new System.Windows.Forms.Button();
            this.statusStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // premiumCheckBox
            // 
            this.premiumCheckBox.AutoSize = true;
            this.premiumCheckBox.Location = new System.Drawing.Point(12, 12);
            this.premiumCheckBox.Name = "premiumCheckBox";
            this.premiumCheckBox.Size = new System.Drawing.Size(97, 17);
            this.premiumCheckBox.TabIndex = 0;
            this.premiumCheckBox.Text = "Premium Case";
            this.premiumCheckBox.UseVisualStyleBackColor = true;
            // 
            // internationalCheckBox
            // 
            this.internationalCheckBox.AutoSize = true;
            this.internationalCheckBox.Location = new System.Drawing.Point(12, 35);
            this.internationalCheckBox.Name = "internationalCheckBox";
            this.internationalCheckBox.Size = new System.Drawing.Size(120, 17);
            this.internationalCheckBox.TabIndex = 1;
            this.internationalCheckBox.Text = "International Case";
            this.internationalCheckBox.UseVisualStyleBackColor = true;
            // 
            // caseComboBox
            // 
            this.caseComboBox.FormattingEnabled = true;
            this.caseComboBox.Location = new System.Drawing.Point(12, 59);
            this.caseComboBox.Name = "caseComboBox";
            this.caseComboBox.Size = new System.Drawing.Size(136, 21);
            this.caseComboBox.TabIndex = 2;
            // 
            // caseButton
            // 
            this.caseButton.Location = new System.Drawing.Point(171, 57);
            this.caseButton.Name = "caseButton";
            this.caseButton.Size = new System.Drawing.Size(110, 23);
            this.caseButton.TabIndex = 3;
            this.caseButton.Text = "Case";
            this.caseButton.UseVisualStyleBackColor = true;
            this.caseButton.Click += new System.EventHandler(this.caseButton_Click);
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.timerToolStripStatusLabel});
            this.statusStrip1.Location = new System.Drawing.Point(0, 179);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(401, 22);
            this.statusStrip1.TabIndex = 4;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // timerToolStripStatusLabel
            // 
            this.timerToolStripStatusLabel.Name = "timerToolStripStatusLabel";
            this.timerToolStripStatusLabel.Size = new System.Drawing.Size(144, 17);
            this.timerToolStripStatusLabel.Text = "Currently Running Timer: ";
            // 
            // collaborationButton
            // 
            this.collaborationButton.Location = new System.Drawing.Point(171, 96);
            this.collaborationButton.Name = "collaborationButton";
            this.collaborationButton.Size = new System.Drawing.Size(110, 23);
            this.collaborationButton.TabIndex = 5;
            this.collaborationButton.Text = "Collaboration / KT";
            this.collaborationButton.UseVisualStyleBackColor = true;
            this.collaborationButton.Click += new System.EventHandler(this.collaborationButton_Click);
            // 
            // meetingButton
            // 
            this.meetingButton.Location = new System.Drawing.Point(171, 135);
            this.meetingButton.Name = "meetingButton";
            this.meetingButton.Size = new System.Drawing.Size(110, 23);
            this.meetingButton.TabIndex = 6;
            this.meetingButton.Text = "Meetings";
            this.meetingButton.UseVisualStyleBackColor = true;
            this.meetingButton.Click += new System.EventHandler(this.meetingButton_Click);
            // 
            // caseLabel
            // 
            this.caseLabel.AutoSize = true;
            this.caseLabel.Location = new System.Drawing.Point(315, 62);
            this.caseLabel.Name = "caseLabel";
            this.caseLabel.Size = new System.Drawing.Size(38, 13);
            this.caseLabel.TabIndex = 7;
            this.caseLabel.Text = "label1";
            // 
            // collaborationLabel
            // 
            this.collaborationLabel.AutoSize = true;
            this.collaborationLabel.Location = new System.Drawing.Point(315, 101);
            this.collaborationLabel.Name = "collaborationLabel";
            this.collaborationLabel.Size = new System.Drawing.Size(38, 13);
            this.collaborationLabel.TabIndex = 8;
            this.collaborationLabel.Text = "label2";
            // 
            // meetingLabel
            // 
            this.meetingLabel.AutoSize = true;
            this.meetingLabel.Location = new System.Drawing.Point(315, 140);
            this.meetingLabel.Name = "meetingLabel";
            this.meetingLabel.Size = new System.Drawing.Size(38, 13);
            this.meetingLabel.TabIndex = 9;
            this.meetingLabel.Text = "label3";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // DescriptiveLabel
            // 
            this.DescriptiveLabel.AutoSize = true;
            this.DescriptiveLabel.Location = new System.Drawing.Point(197, 13);
            this.DescriptiveLabel.Name = "DescriptiveLabel";
            this.DescriptiveLabel.Size = new System.Drawing.Size(61, 13);
            this.DescriptiveLabel.TabIndex = 10;
            this.DescriptiveLabel.Text = "Total Time:";
            // 
            // totalTimeLabel
            // 
            this.totalTimeLabel.AutoSize = true;
            this.totalTimeLabel.Location = new System.Drawing.Point(315, 13);
            this.totalTimeLabel.Name = "totalTimeLabel";
            this.totalTimeLabel.Size = new System.Drawing.Size(38, 13);
            this.totalTimeLabel.TabIndex = 11;
            this.totalTimeLabel.Text = "label1";
            // 
            // lunchButton
            // 
            this.lunchButton.Location = new System.Drawing.Point(22, 135);
            this.lunchButton.Name = "lunchButton";
            this.lunchButton.Size = new System.Drawing.Size(110, 23);
            this.lunchButton.TabIndex = 12;
            this.lunchButton.Text = "Lunch / Break";
            this.lunchButton.UseVisualStyleBackColor = true;
            this.lunchButton.Click += new System.EventHandler(this.lunchButton_Click);
            // 
            // TimeCardHelper
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(401, 201);
            this.Controls.Add(this.lunchButton);
            this.Controls.Add(this.totalTimeLabel);
            this.Controls.Add(this.DescriptiveLabel);
            this.Controls.Add(this.meetingLabel);
            this.Controls.Add(this.collaborationLabel);
            this.Controls.Add(this.caseLabel);
            this.Controls.Add(this.meetingButton);
            this.Controls.Add(this.collaborationButton);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.caseButton);
            this.Controls.Add(this.caseComboBox);
            this.Controls.Add(this.internationalCheckBox);
            this.Controls.Add(this.premiumCheckBox);
            this.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "TimeCardHelper";
            this.Text = "Time Card Helper";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.TimeCardHelper_FormClosing);
            this.Shown += new System.EventHandler(this.TimeCardHelper_Shown);
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.CheckBox premiumCheckBox;
        private System.Windows.Forms.CheckBox internationalCheckBox;
        private System.Windows.Forms.ComboBox caseComboBox;
        private System.Windows.Forms.Button caseButton;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel timerToolStripStatusLabel;
        private System.Windows.Forms.Button collaborationButton;
        private System.Windows.Forms.Button meetingButton;
        private System.Windows.Forms.Label caseLabel;
        private System.Windows.Forms.Label collaborationLabel;
        private System.Windows.Forms.Label meetingLabel;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label DescriptiveLabel;
        private System.Windows.Forms.Label totalTimeLabel;
        private System.Windows.Forms.Button lunchButton;
    }
}

