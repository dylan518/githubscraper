import java.util.Arrays;

/**
 * Task #5 (lesson2)
 * @author Alexander Butkevich
 */
public class Runner2_ht5 {
    /**
     * работа с двумерным массивом int[5][5] #1
     */
    public static void main(String[] args) {

        // объявление и создание массива
        int[][] arr = new int[5][5];

        // вспомогательные переменные
        int minRand = -10;
        int maxRand = 10;
        int[] sumRow = new int[arr.length];
        int[] sumCol = new int[arr[0].length];
        int sum = 0;
        int minRow = 0;
        int maxRow = 0;
        int minCol = 0;
        int maxCol = 0;
        boolean[] swappedRow = new boolean[arr.length];


        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {

                // инициализация массива случайными значениями
                arr[i][j] = (int)(Math.random() * (maxRand - minRand + 1)) + minRand;

                // расчет сумм: всего массива, строк, столбцов
                sum += arr[i][j];
                sumRow[i] += arr[i][j];
                sumCol[j] += arr[i][j];

                // поиск максимального, минимального элементов
                if (arr[i][j] > arr[maxRow][maxCol]) {
                    maxRow = i;
                    maxCol = j;
                }
                if (arr[i][j] < arr[minRow][minCol]) {
                    minRow = i;
                    minCol = j;
                }

            }
        }

        // вывод исходного массива в консоль с суммами строк и столбцов
        System.out.println("array:");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.printf("%7d", arr[i][j]);
            }
            System.out.printf("|%7d\n", sumRow[i]);
        }
        System.out.println("___________________________________|_______");
        for (int col: sumCol){
            System.out.printf("%7d", col);
        }

        // вывод суммы всего массива
        System.out.printf("|%7d <- total\n", sum);

        // замена местами максимального, минимального элементов
        int tmp = arr[minRow][minCol];
        arr[minRow][minCol] = arr[maxRow][maxCol];
        arr[maxRow][maxCol] = tmp;
        System.out.printf("\nmin %d (%d;%d) has swapped with max %d (%d;%d)\n",
                arr[maxRow][maxCol], minRow + 1, minCol + 1,
                arr[minRow][minCol], maxRow + 1, maxCol + 1);

        // замена местами первого нулевого и последнего отрицательного
        // элементов в каждой строке
        for (int i = 0; i < arr.length; i++) {
            int fZeroInd = -1;
            int lNegInd = -1;
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] == 0 && fZeroInd == -1) {
                    fZeroInd = j;
                }
                if (arr[i][j] < 0) {
                    lNegInd = j;
                }
            }
            if (fZeroInd != -1 && lNegInd != -1) {
                swappedRow[i] = true;
                tmp = arr[i][fZeroInd];
                arr[i][fZeroInd] = arr[i][lNegInd];
                arr[i][lNegInd] = tmp;
            } else {
                swappedRow[i] = false;
            }
        }

        // вывод полученного массива в консоль
        System.out.println("\nnew array:");
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.printf("%7d", arr[i][j]);
            }
            if (swappedRow[i]) {
                System.out.println("   1st zero swapped with last negative");
            } else {
                System.out.println();
            }
        }
    }
}
