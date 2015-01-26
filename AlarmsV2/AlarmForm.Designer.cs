namespace Alarms
{
    partial class AlarmForm
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
            this.alarmLabel = new System.Windows.Forms.Label();
            this.categoryLabel = new System.Windows.Forms.Label();
            this.hourNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.hourLabel = new System.Windows.Forms.Label();
            this.minuteNumericUpDown = new System.Windows.Forms.NumericUpDown();
            this.minuteLabel = new System.Windows.Forms.Label();
            this.categoryComboBox = new System.Windows.Forms.ComboBox();
            this.enabledCheckBox = new System.Windows.Forms.CheckBox();
            this.errorLabel = new System.Windows.Forms.Label();
            this.okButton = new System.Windows.Forms.Button();
            this.cancelButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.hourNumericUpDown)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.minuteNumericUpDown)).BeginInit();
            this.SuspendLayout();
            // 
            // alarmLabel
            // 
            this.alarmLabel.AutoSize = true;
            this.alarmLabel.Location = new System.Drawing.Point(21, 19);
            this.alarmLabel.Name = "alarmLabel";
            this.alarmLabel.Size = new System.Drawing.Size(42, 15);
            this.alarmLabel.TabIndex = 0;
            this.alarmLabel.Text = "Alarm:";
            // 
            // categoryLabel
            // 
            this.categoryLabel.AutoSize = true;
            this.categoryLabel.Location = new System.Drawing.Point(21, 52);
            this.categoryLabel.Name = "categoryLabel";
            this.categoryLabel.Size = new System.Drawing.Size(58, 15);
            this.categoryLabel.TabIndex = 1;
            this.categoryLabel.Text = "Category:";
            // 
            // hourNumericUpDown
            // 
            this.hourNumericUpDown.Location = new System.Drawing.Point(118, 17);
            this.hourNumericUpDown.Name = "hourNumericUpDown";
            this.hourNumericUpDown.Size = new System.Drawing.Size(39, 23);
            this.hourNumericUpDown.TabIndex = 2;
            // 
            // hourLabel
            // 
            this.hourLabel.AutoSize = true;
            this.hourLabel.Location = new System.Drawing.Point(163, 19);
            this.hourLabel.Name = "hourLabel";
            this.hourLabel.Size = new System.Drawing.Size(23, 15);
            this.hourLabel.TabIndex = 3;
            this.hourLabel.Text = "Hr.";
            // 
            // minuteNumericUpDown
            // 
            this.minuteNumericUpDown.Location = new System.Drawing.Point(192, 17);
            this.minuteNumericUpDown.Name = "minuteNumericUpDown";
            this.minuteNumericUpDown.Size = new System.Drawing.Size(39, 23);
            this.minuteNumericUpDown.TabIndex = 4;
            // 
            // minuteLabel
            // 
            this.minuteLabel.AutoSize = true;
            this.minuteLabel.Location = new System.Drawing.Point(237, 19);
            this.minuteLabel.Name = "minuteLabel";
            this.minuteLabel.Size = new System.Drawing.Size(31, 15);
            this.minuteLabel.TabIndex = 5;
            this.minuteLabel.Text = "Min.";
            // 
            // categoryComboBox
            // 
            this.categoryComboBox.FormattingEnabled = true;
            this.categoryComboBox.Items.AddRange(new object[] {
            "Personal",
            "Business"});
            this.categoryComboBox.Location = new System.Drawing.Point(118, 49);
            this.categoryComboBox.Name = "categoryComboBox";
            this.categoryComboBox.Size = new System.Drawing.Size(188, 23);
            this.categoryComboBox.TabIndex = 6;
            // 
            // enabledCheckBox
            // 
            this.enabledCheckBox.AutoSize = true;
            this.enabledCheckBox.Location = new System.Drawing.Point(118, 78);
            this.enabledCheckBox.Name = "enabledCheckBox";
            this.enabledCheckBox.Size = new System.Drawing.Size(68, 19);
            this.enabledCheckBox.TabIndex = 7;
            this.enabledCheckBox.Text = "Enabled";
            this.enabledCheckBox.UseVisualStyleBackColor = true;
            // 
            // errorLabel
            // 
            this.errorLabel.AutoSize = true;
            this.errorLabel.Location = new System.Drawing.Point(115, 114);
            this.errorLabel.Name = "errorLabel";
            this.errorLabel.Size = new System.Drawing.Size(66, 15);
            this.errorLabel.TabIndex = 8;
            this.errorLabel.Text = "New Alarm";
            // 
            // okButton
            // 
            this.okButton.Location = new System.Drawing.Point(64, 162);
            this.okButton.Name = "okButton";
            this.okButton.Size = new System.Drawing.Size(75, 23);
            this.okButton.TabIndex = 9;
            this.okButton.Text = "&Ok";
            this.okButton.UseVisualStyleBackColor = true;
            this.okButton.Click += new System.EventHandler(this.okButton_Click);
            // 
            // cancelButton
            // 
            this.cancelButton.Location = new System.Drawing.Point(166, 162);
            this.cancelButton.Name = "cancelButton";
            this.cancelButton.Size = new System.Drawing.Size(75, 23);
            this.cancelButton.TabIndex = 10;
            this.cancelButton.Text = "&Cancel";
            this.cancelButton.UseVisualStyleBackColor = true;
            this.cancelButton.Click += new System.EventHandler(this.cancelButton_Click);
            // 
            // AlarmForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(318, 199);
            this.Controls.Add(this.cancelButton);
            this.Controls.Add(this.okButton);
            this.Controls.Add(this.errorLabel);
            this.Controls.Add(this.enabledCheckBox);
            this.Controls.Add(this.categoryComboBox);
            this.Controls.Add(this.minuteLabel);
            this.Controls.Add(this.minuteNumericUpDown);
            this.Controls.Add(this.hourLabel);
            this.Controls.Add(this.hourNumericUpDown);
            this.Controls.Add(this.categoryLabel);
            this.Controls.Add(this.alarmLabel);
            this.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Name = "AlarmForm";
            this.Text = "Alarm";
            this.Shown += new System.EventHandler(this.AlarmForm_Shown);
            ((System.ComponentModel.ISupportInitialize)(this.hourNumericUpDown)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.minuteNumericUpDown)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label alarmLabel;
        private System.Windows.Forms.Label categoryLabel;
        private System.Windows.Forms.NumericUpDown hourNumericUpDown;
        private System.Windows.Forms.Label hourLabel;
        private System.Windows.Forms.NumericUpDown minuteNumericUpDown;
        private System.Windows.Forms.Label minuteLabel;
        private System.Windows.Forms.ComboBox categoryComboBox;
        private System.Windows.Forms.CheckBox enabledCheckBox;
        private System.Windows.Forms.Label errorLabel;
        private System.Windows.Forms.Button okButton;
        private System.Windows.Forms.Button cancelButton;
    }
}