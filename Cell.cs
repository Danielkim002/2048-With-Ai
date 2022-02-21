using System.Drawing;
class Cell {

    int number;
    Color color;
    public Cell() {
        this.number = 0;
        this.color = Color.White;
    }

    public int GetNumber() {
        return number;
    }

    public void SetNumber(int n) {
        number = n;
    }
}