package JavaLec_0328_Week4;

import java.util.ArrayList;
import java.util.Arrays;

public class MultiDimArray {
    public static void main(String[] args) {
        int numOfLotto = 6;
        int numOfSet = 5;
        int maxNumOfLotto = 45;

        int[][] randArray = new int[numOfSet][numOfLotto]; // set, 갯수

        MakeArray(randArray);
        SortArray(randArray);
        printArray(randArray);
    }

    private static void SortArray(int[][] randArray) {
        for (int i = 0; i < randArray.length; i++)
        {
            Arrays.sort(randArray[i]);
        }
    }

    private static void printArray(int[][] randArray) {
        int s = 0;
        for (int i = 0; i < randArray.length; i++)
        {
            s += 1;
            System.out.print("로또 번호 생성 " + s + "번째 세트 :");
            for(int j = 0; j < randArray[i].length; j++)
            {
                System.out.print(randArray[i][j] + " ");
            }
            System.out.println();
        }
    }
    private static void MakeArray(int[][] randArray) {
        for(int i = 0; i < randArray.length; i++)
        {
            for(int j = 0; j < randArray[i].length; j++)
            {
                randArray[i][j] = (int) (Math.random()*45 +1);
                for(int k = 0; k < j; k++)
                {
                    if(randArray[i][k] == randArray[i][j])
                    {
                        j--;
                        break;
                    }
                }
            }
        }
    }
}
