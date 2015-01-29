namespace whatDidIDoToday
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
            this.collaborationButton = new System.Windows.Forms.Button();
            this.caseDomesticButton = new System.Windows.Forms.Button();
            this.collaborationLabel = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.caseDomesticLabel = new System.Windows.Forms.Label();
            this.meetingButton = new System.Windows.Forms.Button();
            this.meetingsLabel = new System.Windows.Forms.Label();
            this.totalTimeLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // collaborationButton
            // 
            this.collaborationButton.Location = new System.Drawing.Point(13, 24);
            this.collaborationButton.Name = "collaborationButton";
            this.collaborationButton.Size = new System.Drawing.Size(192, 23);
            this.collaborationButton.TabIndex = 0;
            this.collaborationButton.Text = "Collaboration/KnowledgeTransfer";
            this.collaborationButton.UseVisualStyleBackColor = true;
            this.collaborationButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // caseDomesticButton
            // 
            this.caseDomesticButton.Location = new System.Drawing.Point(247, 24);
            this.caseDomesticButton.Name = "caseDomesticButton";
            this.caseDomesticButton.Size = new System.Drawing.Size(119, 23);
            this.caseDomesticButton.TabIndex = 1;
            this.caseDomesticButton.Text = "Case - Domestic";
            this.caseDomesticButton.UseVisualStyleBackColor = true;
            this.caseDomesticButton.Click += new System.EventHandler(this.button2_Click);
            // 
            // collaborationLabel
            // 
            this.collaborationLabel.AutoSize = true;
            this.collaborationLabel.Location = new System.Drawing.Point(13, 67);
            this.collaborationLabel.Name = "collaborationLabel";
            this.collaborationLabel.Size = new System.Drawing.Size(35, 13);
            this.collaborationLabel.TabIndex = 2;
            this.collaborationLabel.Text = "label1";
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // caseDomesticLabel
            // 
            this.caseDomesticLabel.AutoSize = true;
            this.caseDomesticLabel.Location = new System.Drawing.Point(247, 67);
            this.caseDomesticLabel.Name = "caseDomesticLabel";
            this.caseDomesticLabel.Size = new System.Drawing.Size(100, 13);
            this.caseDomesticLabel.TabIndex = 3;
            this.caseDomesticLabel.Text = "caseDomesticLabel";
            // 
            // meetingButton
            // 
            this.meetingButton.Location = new System.Drawing.Point(405, 24);
            this.meetingButton.Name = "meetingButton";
            this.meetingButton.Size = new System.Drawing.Size(135, 23);
            this.meetingButton.TabIndex = 4;
            this.meetingButton.Text = "Meetings";
            this.meetingButton.UseVisualStyleBackColor = true;
            this.meetingButton.Click += new System.EventHandler(this.meetingButton_Click);
            // 
            // meetingsLabel
            // 
            this.meetingsLabel.AutoSize = true;
            this.meetingsLabel.Location = new System.Drawing.Point(405, 67);
            this.meetingsLabel.Name = "meetingsLabel";
            this.meetingsLabel.Size = new System.Drawing.Size(75, 13);
            this.meetingsLabel.TabIndex = 5;
            this.meetingsLabel.Text = "meetingsLabel";
            // 
            // totalTimeLabel
            // 
            this.totalTimeLabel.AutoSize = true;
            this.totalTimeLabel.Location = new System.Drawing.Point(16, 179);
            this.totalTimeLabel.Name = "totalTimeLabel";
            this.totalTimeLabel.Size = new System.Drawing.Size(35, 13);
            this.totalTimeLabel.TabIndex = 6;
            this.totalTimeLabel.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(756, 220);
            this.Controls.Add(this.totalTimeLabel);
            this.Controls.Add(this.meetingsLabel);
            this.Controls.Add(this.meetingButton);
            this.Controls.Add(this.caseDomesticLabel);
            this.Controls.Add(this.collaborationLabel);
            this.Controls.Add(this.caseDomesticButton);
            this.Controls.Add(this.collaborationButton);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Form1_FormClosing);
            this.Shown += new System.EventHandler(this.Form1_Shown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button collaborationButton;
        private System.Windows.Forms.Button caseDomesticButton;
        private System.Windows.Forms.Label collaborationLabel;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label caseDomesticLabel;
        private System.Windows.Forms.Button meetingButton;
        private System.Windows.Forms.Label meetingsLabel;
        private System.Windows.Forms.Label totalTimeLabel;
    }
}

