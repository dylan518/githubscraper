package Ajedrez;

public class Casillas {
    int columns;
    int rows;

    public Casillas(int rows, int columns){
        this.columns = columns;
        this.rows = rows;
    }

    public String getSymbols() {
        if ((rows + columns) % 2 == 0) {
            return "-";
        } else {
            return ".";
        }
    }
}
