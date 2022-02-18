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
        while(true) {
            x++;
            y++;
            Console.WriteLine(x);
            Thread.Sleep(50);
            this.Update();
        }
    }

    private void GUI_Paint(object sender, PaintEventArgs e) {
        Draw(e);
    }

    private void Clear_Paint(object sender, PaintEventArgs e) {
        Clean(e);
    }

    private void Draw(PaintEventArgs e) {
        while(true) {
            e.Graphics.DrawRectangle(new Pen(Color.Black, 3), x, y, 5, 5);
            Thread.Sleep(100);
            Clean(e);
        }
    }

    private void Clean(PaintEventArgs e) {
        e.Graphics.Clear(BackgroundColor);
    }


}

class Program {
    public static void Main(String[] args) {
        GUI gui = new GUI();
        Thread thread = new Thread(gui.UpdateGame);
        thread.Start();
        Application.Run(gui);
        thread.Abort();
        System.Console.WriteLine("Hello!");
        gui.UpdateGame();
        gui.Update();
    }
}