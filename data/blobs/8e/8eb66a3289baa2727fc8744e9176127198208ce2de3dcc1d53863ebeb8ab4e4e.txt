public class MatrixPaths {
    public static void main(String[] args){
        int[][] test = new int[][]{ { 1, 2},
                                    { 3, 4},
                                    { 6, -10} };
        System.out.println(sum(test));
    }

    public static int sum(int[][] matrix){
        int suma = matrix[0][matrix[0].length - 1];
        int i = 0;
        int j = matrix[0].length - 1;
        while(i < matrix.length - 1 && j > 0){
            if(matrix[i + 1][j] > matrix[i][j - 1]){
                suma+= matrix[i + 1][j];
                i++;
            }
            else{
                suma+= matrix[i][j - 1];
                j--;
            }
        }
        suma += matrix[matrix.length - 1][0];
        return suma;
    }
}
