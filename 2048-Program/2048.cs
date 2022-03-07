using System;
using System.Windows.Forms;
using System.Diagnostics;
using System.IO;
using System.Threading;
using Newtonsoft.Json;
using System.Drawing;

public class Program {

    private static GUI Gui;
    private static String LocalDirectory;
    public static Panel gamePanel;

    public static void Main(String[] args) {
        gamePanel = new Panel();
        GetGamePanel();
        Gui = new GUI();
        //This for loop is to go back 4 directories to get to the root directory of the program

        //Thread thread = new Thread(RunPythonThread);
        //thread.Start();
        Application.Run(Gui);
    }


    /*
    public static void RunPythonThread() {
        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = @"C:\Users\Justin\AppData\Local\Programs\Python\Python37-32\python.exe";
        var MainPython = @"C:\Users\Justin\Desktop\2048-With-AI\Main.py";
        start.Arguments = MainPython;

        start.UseShellExecute = false;
        start.CreateNoWindow = true;
        start.RedirectStandardOutput = true;
        start.RedirectStandardInput = true;
        start.RedirectStandardError = true;

        var errors = "";
        var results = "";
        using(Process process = Process.Start(start)) {
            errors = process.StandardError.ReadToEnd();
            results = process.StandardOutput.ReadToEnd();
            System.Console.WriteLine(results);
        }
    }

    public static void UpdateCellValues() {
        int[,] _numbers = new int[4,4];
    }
    */

    public static void GetGamePanel() {
        LocalDirectory = Directory.GetCurrentDirectory();
        for (int i = 0; i < 4; i++)
        {
            LocalDirectory = Directory.GetParent(LocalDirectory).ToString();
        }
        String fileName = "GamePanel.json";
        using(FileStream fileStream = new FileStream(
            LocalDirectory + "\\" + fileName, FileMode.Open,
            FileAccess.Read, FileShare.ReadWrite))
        {
            String json;
            using(StreamReader sr = new StreamReader(fileStream))
            {
                json = sr.ReadToEnd();
                sr.Close();
            }
            fileStream.Close();
            dynamic cells = JsonConvert.DeserializeObject<dynamic>(json);
            int x = 0;
            int y = 0;
            int[,] b = JsonConvert.DeserializeObject<int[,]>(json);
            if(b == null)
            {
                return;
            }
            foreach (int i in b)
            {
                gamePanel.matrix[x, y] = new Cell
                {
                    number = i,
                    color = Color.White
                };
                x++;
                if (x >= 4)
                {
                    x = 0;
                    y++;
                }
            }
        }
    }    
}