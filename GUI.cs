using System;
using System.Windows.Forms;
using System.Threading;
using System.Drawing;

class GUI : Form {

    int x = 0;
    int y = 0;

    Panel panel = new Panel();
    Color BackgroundColor = Color.FromArgb(255, 248, 230);
    String TitleName = "2048 With Machine Learning";
    Size MinSize = new Size(720, 480);

    public GUI() {
        this.BackColor = BackgroundColor;
        this.Text = TitleName;
        this.MinimumSize = MinSize;
    }

    public void UpdateGame() {
        this.Paint += new PaintEventHandler(this.GUI_Paint);
        x++;
        y++;
        this.Invalidate();
    }

    private void GUI_Paint(object sender, PaintEventArgs e) {
        Draw(e);
    }

    private void Draw(PaintEventArgs e) {
        e.Graphics.DrawRectangle(new Pen(Color.Black, 3), x, y, 5, 5);
    }
}

class Program {
    public static void Main(String[] args) {
        GUI gui = new GUI();
        ThreadWork.Gui = gui;
        Thread thread = new Thread(ThreadWork.DoWork);
        thread.Start();
        Application.Run(gui);
        thread.Abort();
    }
}

class ThreadWork {

    public static GUI Gui;
    public static void DoWork() {
        while(true) {
            Gui.UpdateGame();
            Thread.Sleep(16);
        }
    }
}