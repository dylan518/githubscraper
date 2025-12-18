import java.util.Formatter;
import java.util.Random;
import java.io.*;
import java.util.Scanner;
public class Board {

    private Utils util = new Utils();
    private Random rand = new Random();
    private Formatter f = new Formatter();
    private String boardData[][] = new String[8][8];
    private String allThemeWords[] = new String[50];
    
    public int boardSize;
    public char theme;
    
    
    public Boolean isMatch(int row1, int col1, int row2, int col2) {
        return boardData[row1][col1] == boardData[row2][col2];
    }
    
    public String getElement(int row, int col){
        return boardData[row][col];
    }
    
    public void loadAllThemeWords() throws FileNotFoundException {
        String path = null;
        if (theme == 'c') {
            path = "./themes/Cars.txt";
        }
        else if (theme == 'e') {
            path = "./themes/Atoms.txt";
        }
        else  if (theme == 'f') {
            path = "./themes/Fruit.txt";
        }
        File read = new File(path);
        Scanner handler = new Scanner(read);
        int i = 0;
        while (handler.hasNextLine()) {
            allThemeWords[i] = handler.nextLine();
            i++;
        }
        handler.close();
    }

    
    public void printBoard(String guessedThemeWords[], int rowGuess1, int columnGuess1, int rowGuess2, int columnGuess2) {
        int uniqueWordCount = boardSize * boardSize / 2;
        for (int i = 1; i < 100; i++) {
            System.out.println();
        }
        for(int row = 0; row < boardSize; row++){
            for(int column = 0; column < boardSize; column++){
                if (util.contains(guessedThemeWords, uniqueWordCount, boardData[row][column])){
                    System.out.print(f.format("%9s", boardData[row][column]));
                    f = new Formatter();
                }
                else if ((row == rowGuess1 && column == columnGuess1) || (row == rowGuess2 && column == columnGuess2)){
                    System.out.print(f.format("%9s", boardData[row][column]));
                    f = new Formatter();
                }
                else {
                    System.out.print(f.format("%9c", '▢'));
                    f = new Formatter();
                }
            }
            System.out.println("\n");
        }
    }
    
    void initializeBoard() throws FileNotFoundException {
        
        int count = 0;
        int uniqueWordCount = boardSize * boardSize / 2;
        String selectedThemeWords[] = new String[32];
        loadAllThemeWords();
        
        while (count < uniqueWordCount) {
            
            int index = rand.nextInt(50);
            if (allThemeWords[index] != "") {
                selectedThemeWords[count] = allThemeWords[index];
                allThemeWords[index] = "";
                count++;
            }
        }
        
        String doubleSelectedThemeWords[] = new String[64];
        for(int i = 0; i < uniqueWordCount; i++){
            doubleSelectedThemeWords[i] = selectedThemeWords[i];
            doubleSelectedThemeWords[i+uniqueWordCount] = selectedThemeWords[i];
        }
        
        util.shuffleArrayInPlace(doubleSelectedThemeWords, 16);
        
        
        int i = 0;
        for(int row = 0; row < boardSize; row++) {
            for(int column = 0; column < boardSize; column++){
                boardData[row][column] = doubleSelectedThemeWords[i];
                i++;
            }
        }
    }
};
