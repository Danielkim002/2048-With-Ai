class Panel {

    Cell[,] matrix = new Cell[4, 4];

    public Panel() {
        for(int r = 0; r < 4; r++) {
            for(int c = 0; c < 4; c++) {
                matrix[r, c] = new Cell();
            }
        }   
    }

    public Cell[,] getMatrix() {
        return matrix;
    }
}