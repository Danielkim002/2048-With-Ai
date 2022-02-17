using System;
using System.Windows.Forms;
using System.Drawing;

class GUI : Form {

    Color BackgroundColor = Color.FromArgb(255, 248, 230);
    String TitleName = "2048 With Machine Learning";
    Size MinSize = new Size(720, 480);
    public GUI() {
        this.BackColor = BackgroundColor;
        this.Text = TitleName;
        this.MinimumSize = MinSize;
    }
}

class Program {
    public static void Main(String[] args) {
        GUI gui = new GUI();
        Application.Run(gui);
    }
}