namespace CreditQuest
{
    partial class creidtConsumption
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
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.usernameTextBoc = new System.Windows.Forms.TextBox();
            this.passwordTextBox = new System.Windows.Forms.TextBox();
            this.creditButton = new System.Windows.Forms.Button();
            this.creditListBox = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 32);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(58, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Username:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(16, 70);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(56, 13);
            this.label2.TabIndex = 1;
            this.label2.Text = "Password:";
            // 
            // usernameTextBoc
            // 
            this.usernameTextBoc.Location = new System.Drawing.Point(83, 29);
            this.usernameTextBoc.Name = "usernameTextBoc";
            this.usernameTextBoc.Size = new System.Drawing.Size(171, 20);
            this.usernameTextBoc.TabIndex = 3;
            // 
            // passwordTextBox
            // 
            this.passwordTextBox.Location = new System.Drawing.Point(83, 67);
            this.passwordTextBox.Name = "passwordTextBox";
            this.passwordTextBox.PasswordChar = '*';
            this.passwordTextBox.Size = new System.Drawing.Size(171, 20);
            this.passwordTextBox.TabIndex = 4;
            // 
            // creditButton
            // 
            this.creditButton.Location = new System.Drawing.Point(127, 322);
            this.creditButton.Name = "creditButton";
            this.creditButton.Size = new System.Drawing.Size(127, 22);
            this.creditButton.TabIndex = 5;
            this.creditButton.Text = "Get Credit Consumption";
            this.creditButton.UseVisualStyleBackColor = true;
            this.creditButton.Click += new System.EventHandler(this.creditButton_Click);
            // 
            // creditListBox
            // 
            this.creditListBox.FormattingEnabled = true;
            this.creditListBox.Location = new System.Drawing.Point(19, 113);
            this.creditListBox.Name = "creditListBox";
            this.creditListBox.Size = new System.Drawing.Size(235, 199);
            this.creditListBox.TabIndex = 6;
            // 
            // creidtConsumption
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(267, 358);
            this.Controls.Add(this.creditListBox);
            this.Controls.Add(this.creditButton);
            this.Controls.Add(this.passwordTextBox);
            this.Controls.Add(this.usernameTextBoc);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "creidtConsumption";
            this.Text = "Credit Consumption";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox usernameTextBoc;
        private System.Windows.Forms.TextBox passwordTextBox;
        private System.Windows.Forms.Button creditButton;
        private System.Windows.Forms.ListBox creditListBox;
    }
}

