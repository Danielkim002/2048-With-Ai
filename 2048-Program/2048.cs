using System.Windows.Forms;
using System.Diagnostics;
using Newtonsoft.Json;
using System.Drawing;

public class Program {

    private static GUI Gui;
    private static String LocalDirectory;
    public  static Panel gamePanel;
    private static String _pythonPath;

    public static void Main(String[] args) {
        var file = "Configuration.json";

        gamePanel = new Panel();
        GetGamePanel();
        Gui = new GUI();

        GetPythonPath(file);

        Thread thread = new Thread(RunPythonThread);
        thread.Start();
        Gui.initialize();
        Application.Run(Gui);
    }

    public static void RunPythonThread() {
        LocalDirectory = Directory.GetCurrentDirectory();
        for (int i = 0; i < 4; i++)
        {
            LocalDirectory = Directory.GetParent(LocalDirectory).ToString();
        }
        ProcessStartInfo start = new ProcessStartInfo(_pythonPath, LocalDirectory + "\\" + "Main.py");
        start.FileName = @_pythonPath;
        var MainPython = @LocalDirectory + "\\" + "Main.py";

        start.UseShellExecute = false;
        start.CreateNoWindow = true;
        start.RedirectStandardOutput = true;
        start.RedirectStandardInput = true;
        start.RedirectStandardError = true;

        start.WorkingDirectory = @LocalDirectory;

        using (Process process = Process.Start(start)) {
            Console.WriteLine("Starting Python");
            using (StreamReader reader = process.StandardOutput)
            {
                var errors = process.StandardError.ReadToEndAsync();
                var results = reader.ReadToEndAsync();
                Console.WriteLine(errors.Result);
                Console.WriteLine(results.Result);
            }
            Console.WriteLine(process.HasExited);
        }
    }

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
    static void GetPythonPath(String fileName)
    {
        LocalDirectory = Directory.GetCurrentDirectory();

        for (int i = 0; i < 3; i++)
        {
            LocalDirectory = Directory.GetParent(LocalDirectory).ToString();
        }

        Configuration config = new Configuration();
        using (StreamWriter sw = File.AppendText(LocalDirectory + "\\" + fileName))
        {
            String json;
            StreamReader sr = new StreamReader(new FileStream(
            LocalDirectory + "\\" + fileName, FileMode.Open,
            FileAccess.Read, FileShare.ReadWrite));
            json = sr.ReadToEnd();
            config = JsonConvert.DeserializeObject<Configuration>(json);
            if (config == null || config.PythonPath == "")
            {
                config = new Configuration();
                JsonSerializer serializer = new JsonSerializer();
                Console.WriteLine("Enter your path!");
                String input = Console.ReadLine();
                config.PythonPath = input;
                serializer.Serialize(sw, config);
            }
            _pythonPath = config.PythonPath;
        }
    }
}

class Configuration
{
    public String PythonPath;
}