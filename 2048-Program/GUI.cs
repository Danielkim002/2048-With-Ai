using System;
using System.Windows.Forms;
using System.Drawing;
using Microsoft.VisualBasic;

class GUI : Form {

    int x = 0;
    int y = 0;

    Panel GamePanel;
    Color BackgroundColor = Color.FromArgb(255, 248, 230);
    System.Windows.Forms.Timer tmr;

    public GUI() {
        GamePanel = Program.gamePanel;
        //Sets up all properties of the GUI
        this.BackColor = BackgroundColor;
        this.Text = "2048 With Machine Learning";
        this.MinimumSize = new Size(720, 480);
        this.DoubleBuffered = true;

    }

    public void initialize()
    {
        //The eventhandler for painting objects
        Paint += GUI_Paint;

        //Timer for updating the window. Runs in tick intervals of 50ms
        tmr = new System.Windows.Forms.Timer();
        tmr.Interval = 50;
        tmr.Tick += GUI_Tick;
        tmr.Start();
    }

    private void GUI_Tick(object Sender, EventArgs e) {
        Invalidate();
    }

    private void GUI_Paint(object sender, PaintEventArgs e) {
        DrawCells(e);
    }

    private void DrawCells(PaintEventArgs e) {
        Program.GetGamePanel();
        GamePanel = Program.gamePanel;
        int squareLength = (this.Width / 16);
        x = (this.Width / 16)*6;
        y = (this.Height/2) - (squareLength*2);
        int count = 1;
        foreach(Cell cell in GamePanel.matrix) {
            e.Graphics.DrawRectangle(new Pen(Color.Black), x, y, squareLength, squareLength);
            e.Graphics.DrawString("" + cell.number, new Font("Arial", 16), new SolidBrush(Color.Black), x + (squareLength/2), y + ((squareLength/2)));
            x += squareLength;
            if(count % 4 == 0) {
                x = (this.Width / 16)*6;
                y+=squareLength;
            }
            count++;
        }
    }
}