using System;
using System.Windows.Forms;
using System.Drawing;

class GUI : Form {

    public GUI() {
        this.Name = "Example";
        this.MinimumSize = new Size(720, 480);
    }
}

class Program {

    public static void Main(String[] args) {
        GUI gui = new GUI();
        Application.Run(gui);
    }
}