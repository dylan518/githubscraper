package p04VectorsAndMatrix;

import java.util.Scanner;

public class Task04 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        float[][] matrix = new float[10][4];
        float[] average = new float[10];
        float sum = 0.0f;

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 4; j++) {
                System.out.printf("\nDigite numero da linha %d e coluna %d: ", i, j);
                matrix[i][j] = input.nextFloat();
            }
        }

        for (int i = 0; i < 10; i++) {
            sum = 0.0f;
            for (int j = 0; j < 4; j++) {
                sum += matrix[i][j];
            }
            average[i] = sum/4;
        }
        System.out.printf("\nvetor: \n");
        for (int i = 0; i < 10; i++) {
            System.out.printf("%.1f ", average[i]);
        }
    }
}
