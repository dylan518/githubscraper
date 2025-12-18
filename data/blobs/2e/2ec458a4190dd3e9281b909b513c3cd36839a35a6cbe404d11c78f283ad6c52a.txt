import java.util.ArrayList;
import java.util.*;
import java.io.*;
import java.util.Arrays;

public class nQueens2{
    
  public static void main(String[] args) throws Exception {
    Scanner scn = new Scanner(System.in);
    int n = scn.nextInt();
    
    var ans = totalNQueens(n);
    System.out.println(ans);
  }  

  public static int totalNQueens(int n) {
    int ans = solver(n, 0, 0, new int[n], new int[n], new int[2*n - 1], new int[2*n - 1]);
    return ans;
  }
  //now simply call the function nQueens

    public static int solver(int n, int floor, int queensPlaced, int[] rows, int[] cols, int[] d1, int[] d2){
        //combinations solved using for loops let's say
        if(queensPlaced == n){
            return 1;
        }
        
        //there are some more optimisation baby
        //if you are done with this floor, then fucking go the next one!
        int count = 0;
        for(int room = 0; room < n; room++){  //checking at that given floor if someone exists or not
            int row = floor;
            int col = room;
            if(!(rows[row] == 1 || cols[col] == 1 || d1[row + col] == 1 || d2[row - col + n - 1] == 1)){
                rows[row] = 1;
                cols[col] = 1;
                d1[row + col] = 1;
                d2[row - col + n - 1] = 1;

                count += solver(n, floor + 1,  queensPlaced + 1, rows, cols, d1, d2);                

                //demark everything in here
                rows[row] = 0;
                cols[col] = 0;
                d1[row + col] = 0;
                d2[row - col + n - 1] = 0;
            }
        }   

        return count;
    }

}
