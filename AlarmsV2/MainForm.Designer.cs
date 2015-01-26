namespace Alarms
{
    partial class MainForm
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
        	this.currentTimeLabel = new System.Windows.Forms.Label();
        	this.timeLabel = new System.Windows.Forms.Label();
        	this.alarmsLabel = new System.Windows.Forms.Label();
        	this.addButton = new System.Windows.Forms.Button();
        	this.editButton = new System.Windows.Forms.Button();
        	this.deleteButton = new System.Windows.Forms.Button();
        	this.exitButton = new System.Windows.Forms.Button();
        	this.alarmsListBox = new System.Windows.Forms.ListBox();
        	this.alarmTimer = new System.Windows.Forms.Timer(this.components);
        	this.SuspendLayout();
        	// 
        	// currentTimeLabel
        	// 
        	this.currentTimeLabel.AutoSize = true;
        	this.currentTimeLabel.Location = new System.Drawing.Point(12, 18);
        	this.currentTimeLabel.Name = "currentTimeLabel";
        	this.currentTimeLabel.Size = new System.Drawing.Size(80, 15);
        	this.currentTimeLabel.TabIndex = 0;
        	this.currentTimeLabel.Text = "Current Time:";
        	// 
        	// timeLabel
        	// 
        	this.timeLabel.AutoSize = true;
        	this.timeLabel.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.timeLabel.Location = new System.Drawing.Point(108, 18);
        	this.timeLabel.Name = "timeLabel";
        	this.timeLabel.Size = new System.Drawing.Size(77, 15);
        	this.timeLabel.TabIndex = 1;
        	this.timeLabel.Text = "12:00:00 AM";
        	// 
        	// alarmsLabel
        	// 
        	this.alarmsLabel.AutoSize = true;
        	this.alarmsLabel.Location = new System.Drawing.Point(12, 46);
        	this.alarmsLabel.Name = "alarmsLabel";
        	this.alarmsLabel.Size = new System.Drawing.Size(44, 15);
        	this.alarmsLabel.TabIndex = 2;
        	this.alarmsLabel.Text = "Alarms";
        	// 
        	// addButton
        	// 
        	this.addButton.Location = new System.Drawing.Point(244, 77);
        	this.addButton.Name = "addButton";
        	this.addButton.Size = new System.Drawing.Size(75, 23);
        	this.addButton.TabIndex = 3;
        	this.addButton.Text = "&Add";
        	this.addButton.UseVisualStyleBackColor = true;
        	this.addButton.Click += new System.EventHandler(this.addButton_Click);
        	// 
        	// editButton
        	// 
        	this.editButton.Location = new System.Drawing.Point(244, 118);
        	this.editButton.Name = "editButton";
        	this.editButton.Size = new System.Drawing.Size(75, 23);
        	this.editButton.TabIndex = 4;
        	this.editButton.Text = "&Edit";
        	this.editButton.UseVisualStyleBackColor = true;
        	this.editButton.Click += new System.EventHandler(this.editButton_Click);
        	// 
        	// deleteButton
        	// 
        	this.deleteButton.Location = new System.Drawing.Point(244, 160);
        	this.deleteButton.Name = "deleteButton";
        	this.deleteButton.Size = new System.Drawing.Size(75, 23);
        	this.deleteButton.TabIndex = 5;
        	this.deleteButton.Text = "&Delete";
        	this.deleteButton.UseVisualStyleBackColor = true;
        	this.deleteButton.Click += new System.EventHandler(this.deleteButton_Click);
        	// 
        	// exitButton
        	// 
        	this.exitButton.Location = new System.Drawing.Point(244, 267);
        	this.exitButton.Name = "exitButton";
        	this.exitButton.Size = new System.Drawing.Size(75, 23);
        	this.exitButton.TabIndex = 6;
        	this.exitButton.Text = "E&xit";
        	this.exitButton.UseVisualStyleBackColor = true;
        	this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
        	// 
        	// alarmsListBox
        	// 
        	this.alarmsListBox.FormattingEnabled = true;
        	this.alarmsListBox.ItemHeight = 15;
        	this.alarmsListBox.Location = new System.Drawing.Point(15, 63);
        	this.alarmsListBox.Name = "alarmsListBox";
        	this.alarmsListBox.Size = new System.Drawing.Size(207, 229);
        	this.alarmsListBox.TabIndex = 7;
        	this.alarmsListBox.SelectedIndexChanged += new System.EventHandler(this.alarmsListBox_SelectedIndexChanged);
        	// 
        	// alarmTimer
        	// 
        	this.alarmTimer.Interval = 1000;
        	this.alarmTimer.Tick += new System.EventHandler(this.alarmTimer_Tick);
        	// 
        	// MainForm
        	// 
        	this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
        	this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        	this.ClientSize = new System.Drawing.Size(331, 302);
        	this.Controls.Add(this.alarmsListBox);
        	this.Controls.Add(this.exitButton);
        	this.Controls.Add(this.deleteButton);
        	this.Controls.Add(this.editButton);
        	this.Controls.Add(this.addButton);
        	this.Controls.Add(this.alarmsLabel);
        	this.Controls.Add(this.timeLabel);
        	this.Controls.Add(this.currentTimeLabel);
        	this.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
        	this.MaximizeBox = false;
        	this.Name = "MainForm";
        	this.Text = "Alarms";
        	this.Shown += new System.EventHandler(this.MainForm_Shown);
        	this.ResumeLayout(false);
        	this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label currentTimeLabel;
        private System.Windows.Forms.Label timeLabel;
        private System.Windows.Forms.Label alarmsLabel;
        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Button editButton;
        private System.Windows.Forms.Button deleteButton;
        private System.Windows.Forms.Button exitButton;
        private System.Windows.Forms.ListBox alarmsListBox;
        private System.Windows.Forms.Timer alarmTimer;
    }
}

