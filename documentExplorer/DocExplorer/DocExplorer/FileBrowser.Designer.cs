namespace DocExplorer
{
    partial class FileBrowser
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
            this.browserSplitContainer = new System.Windows.Forms.SplitContainer();
            this.folderListBox = new System.Windows.Forms.ListBox();
            this.dataSourceTextBox = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.browserSplitContainer)).BeginInit();
            this.browserSplitContainer.Panel1.SuspendLayout();
            this.browserSplitContainer.Panel2.SuspendLayout();
            this.browserSplitContainer.SuspendLayout();
            this.SuspendLayout();
            // 
            // browserSplitContainer
            // 
            this.browserSplitContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.browserSplitContainer.Location = new System.Drawing.Point(0, 0);
            this.browserSplitContainer.Name = "browserSplitContainer";
            // 
            // browserSplitContainer.Panel1
            // 
            this.browserSplitContainer.Panel1.Controls.Add(this.folderListBox);
            // 
            // browserSplitContainer.Panel2
            // 
            this.browserSplitContainer.Panel2.Controls.Add(this.dataSourceTextBox);
            this.browserSplitContainer.Size = new System.Drawing.Size(844, 534);
            this.browserSplitContainer.SplitterDistance = 281;
            this.browserSplitContainer.TabIndex = 0;
            // 
            // folderListBox
            // 
            this.folderListBox.FormattingEnabled = true;
            this.folderListBox.Location = new System.Drawing.Point(3, 4);
            this.folderListBox.Name = "folderListBox";
            this.folderListBox.Size = new System.Drawing.Size(275, 524);
            this.folderListBox.TabIndex = 0;
            // 
            // dataSourceTextBox
            // 
            this.dataSourceTextBox.Location = new System.Drawing.Point(3, 4);
            this.dataSourceTextBox.Name = "dataSourceTextBox";
            this.dataSourceTextBox.Size = new System.Drawing.Size(553, 22);
            this.dataSourceTextBox.TabIndex = 0;
            // 
            // FileBrowser
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(844, 534);
            this.Controls.Add(this.browserSplitContainer);
            this.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Name = "FileBrowser";
            this.Text = "Form1";
            this.browserSplitContainer.Panel1.ResumeLayout(false);
            this.browserSplitContainer.Panel2.ResumeLayout(false);
            this.browserSplitContainer.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.browserSplitContainer)).EndInit();
            this.browserSplitContainer.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer browserSplitContainer;
        private System.Windows.Forms.ListBox folderListBox;
        private System.Windows.Forms.TextBox dataSourceTextBox;
    }
}

