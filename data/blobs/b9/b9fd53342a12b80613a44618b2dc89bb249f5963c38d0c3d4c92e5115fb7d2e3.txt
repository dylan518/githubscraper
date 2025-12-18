/*-----------------------asked in microsoft, amazon and many other.-------------------------------------------

https://leetcode.com/problems/set-matrix-zeroes/

 Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
 */
import java.util.*;
public class set_matrix_zero {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of rows and columns:");
        int n=sc.nextInt();
        int m=sc.nextInt();
        int nums[][]=new int[n][m];
        System.out.println("Enter the matrix:");
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
               nums[i][j]=sc.nextInt();
            }
        }
        setZeroes(nums);
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
               System.out.print(nums[i][j]);
            }
            System.out.println();
        }
    }

    public static void setZeroes(int[][] matrix) {
        
        //this is to check if their is any zero in 1st row or 1st column 
        boolean row0=false,col0=false;
        
        //this will traverse through 1st element of all the rows and if their is any zeros then col=true 
        for(int i=0;i<matrix.length;i++)
            if(matrix[i][0]==0)
                col0=true;
        //similarly, to check zeros present in the 1st row
        for(int j=0;j<matrix[0].length;j++)
            if(matrix[0][j]==0)
                row0=true;
        
        for(int i=1;i<matrix.length;i++)
        {
            for(int j=1;j<matrix[0].length;j++)
            {
                if(matrix[i][j]==0)
                {
                    matrix[0][j]=0;
                    matrix[i][0]=0;
                }
            }
        }
        
        for(int i=1;i<matrix.length;i++)
        {
            if(matrix[i][0]==0)
            {
                for(int j=0;j<matrix[0].length;j++)
                    matrix[i][j]=0;
            }
        }
        for(int j=1;j<matrix[0].length;j++)
        {
            if(matrix[0][j]==0)
                for(int i=0;i<matrix.length;i++)
                    matrix[i][j]=0;
        }
        
        if(row0)
        {
            for(int j=0;j<matrix[0].length;j++)
                matrix[0][j]=0;
        }
        if(col0)
        {
            for(int i=0;i<matrix.length;i++)
                matrix[i][0]=0;
        }
        
    }
    
}
