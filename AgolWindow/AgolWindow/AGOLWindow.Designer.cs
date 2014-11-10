namespace AgolWindow
{
    partial class AGOLWindow
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
            this.usernameLabel = new System.Windows.Forms.Label();
            this.usernameTextBox = new System.Windows.Forms.TextBox();
            this.passwordLabel = new System.Windows.Forms.Label();
            this.passwordTextBox = new System.Windows.Forms.TextBox();
            this.loginButton = new System.Windows.Forms.Button();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.orgPage = new System.Windows.Forms.TabPage();
            this.servicesPage = new System.Windows.Forms.TabPage();
            this.orgInfoLabel = new System.Windows.Forms.Label();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.windowStatusLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.usersPage = new System.Windows.Forms.TabPage();
            this.tabControl1.SuspendLayout();
            this.orgPage.SuspendLayout();
            this.statusStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // usernameLabel
            // 
            this.usernameLabel.AutoSize = true;
            this.usernameLabel.Location = new System.Drawing.Point(3, 15);
            this.usernameLabel.Name = "usernameLabel";
            this.usernameLabel.Size = new System.Drawing.Size(61, 13);
            this.usernameLabel.TabIndex = 0;
            this.usernameLabel.Text = "Username:";
            // 
            // usernameTextBox
            // 
            this.usernameTextBox.Location = new System.Drawing.Point(70, 12);
            this.usernameTextBox.Name = "usernameTextBox";
            this.usernameTextBox.Size = new System.Drawing.Size(100, 22);
            this.usernameTextBox.TabIndex = 1;
            // 
            // passwordLabel
            // 
            this.passwordLabel.AutoSize = true;
            this.passwordLabel.Location = new System.Drawing.Point(3, 48);
            this.passwordLabel.Name = "passwordLabel";
            this.passwordLabel.Size = new System.Drawing.Size(59, 13);
            this.passwordLabel.TabIndex = 2;
            this.passwordLabel.Text = "Password:";
            // 
            // passwordTextBox
            // 
            this.passwordTextBox.Location = new System.Drawing.Point(70, 45);
            this.passwordTextBox.Name = "passwordTextBox";
            this.passwordTextBox.PasswordChar = '*';
            this.passwordTextBox.Size = new System.Drawing.Size(100, 22);
            this.passwordTextBox.TabIndex = 3;
            // 
            // loginButton
            // 
            this.loginButton.Location = new System.Drawing.Point(190, 28);
            this.loginButton.Name = "loginButton";
            this.loginButton.Size = new System.Drawing.Size(75, 23);
            this.loginButton.TabIndex = 4;
            this.loginButton.Text = "&Login";
            this.loginButton.UseVisualStyleBackColor = true;
            this.loginButton.Click += new System.EventHandler(this.loginButton_Click);
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.orgPage);
            this.tabControl1.Controls.Add(this.servicesPage);
            this.tabControl1.Controls.Add(this.usersPage);
            this.tabControl1.Location = new System.Drawing.Point(6, 73);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(259, 416);
            this.tabControl1.TabIndex = 5;
            // 
            // orgPage
            // 
            this.orgPage.AutoScroll = true;
            this.orgPage.Controls.Add(this.orgInfoLabel);
            this.orgPage.Location = new System.Drawing.Point(4, 22);
            this.orgPage.Name = "orgPage";
            this.orgPage.Padding = new System.Windows.Forms.Padding(3);
            this.orgPage.Size = new System.Drawing.Size(251, 390);
            this.orgPage.TabIndex = 0;
            this.orgPage.Text = "Organization Information";
            this.orgPage.UseVisualStyleBackColor = true;
            // 
            // servicesPage
            // 
            this.servicesPage.AutoScroll = true;
            this.servicesPage.Location = new System.Drawing.Point(4, 22);
            this.servicesPage.Name = "servicesPage";
            this.servicesPage.Padding = new System.Windows.Forms.Padding(3);
            this.servicesPage.Size = new System.Drawing.Size(251, 390);
            this.servicesPage.TabIndex = 1;
            this.servicesPage.Text = "REST Services";
            this.servicesPage.UseVisualStyleBackColor = true;
            // 
            // orgInfoLabel
            // 
            this.orgInfoLabel.AutoSize = true;
            this.orgInfoLabel.Location = new System.Drawing.Point(7, 7);
            this.orgInfoLabel.Name = "orgInfoLabel";
            this.orgInfoLabel.Size = new System.Drawing.Size(236, 13);
            this.orgInfoLabel.TabIndex = 0;
            this.orgInfoLabel.Text = "Information will appear here after you login.";
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.windowStatusLabel});
            this.statusStrip1.Location = new System.Drawing.Point(0, 497);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(273, 22);
            this.statusStrip1.TabIndex = 6;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // windowStatusLabel
            // 
            this.windowStatusLabel.Name = "windowStatusLabel";
            this.windowStatusLabel.Size = new System.Drawing.Size(35, 17);
            this.windowStatusLabel.Text = "Idle...";
            // 
            // usersPage
            // 
            this.usersPage.AutoScroll = true;
            this.usersPage.Location = new System.Drawing.Point(4, 22);
            this.usersPage.Name = "usersPage";
            this.usersPage.Size = new System.Drawing.Size(251, 390);
            this.usersPage.TabIndex = 2;
            this.usersPage.Text = "Users";
            this.usersPage.UseVisualStyleBackColor = true;
            // 
            // AGOLWindow
            // 
            this.AutoScroll = true;
            this.AutoSize = true;
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.tabControl1);
            this.Controls.Add(this.loginButton);
            this.Controls.Add(this.passwordTextBox);
            this.Controls.Add(this.passwordLabel);
            this.Controls.Add(this.usernameTextBox);
            this.Controls.Add(this.usernameLabel);
            this.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Name = "AGOLWindow";
            this.Size = new System.Drawing.Size(273, 519);
            this.tabControl1.ResumeLayout(false);
            this.orgPage.ResumeLayout(false);
            this.orgPage.PerformLayout();
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label usernameLabel;
        private System.Windows.Forms.TextBox usernameTextBox;
        private System.Windows.Forms.Label passwordLabel;
        private System.Windows.Forms.TextBox passwordTextBox;
        private System.Windows.Forms.Button loginButton;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage orgPage;
        private System.Windows.Forms.TabPage servicesPage;
        private System.Windows.Forms.Label orgInfoLabel;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel windowStatusLabel;
        private System.Windows.Forms.TabPage usersPage;

    }
}
