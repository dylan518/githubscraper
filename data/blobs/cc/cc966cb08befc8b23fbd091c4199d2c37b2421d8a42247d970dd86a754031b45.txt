//Jose Trevizo
//CS2050
//Program 6
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Program6 {
    public static void bubbleSort(int array[]){ //bubble sort
        for(int i =0; i < array.length - 1; i++){
            for(int j =0; j < array.length- i - 1; j++){
                if (array[j] > array[j+1]){
                    int temp = array[j];
                    array [j] = array[j+1];
                    array[j+1] = temp;
                }
            }
        }
    }
    public static void selectionSort(int array[]){ //selection sort
        for(int i =0; i < array.length - 1; i++){
            int min = i;
            for(int j = i + 1; j < array.length; j++){
                if(array[min] > array[j]){
                    min = j;
                }
            }
            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;
        }
    }
    public static void bubbleSortString(String array[]){ //bubble sort for Strings
        for(int i = 0 ; i < array.length; i++){
            String temp;
            for (int j = i + 1; j < array.length; j++){
                if(array[j].compareTo(array[i]) < 0){
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }
    }
    public static void selectionSortStrings(String array[]){ //selection sort for Strings
        for(int i =0; i < array.length - 1; i++){
            int min = i;
            for(int j = i + 1; j < array.length; j++){
                if(array[j].compareTo(array[min]) < 0){
                    String temp = array[i];
                    array[i] = array[min];
                    array[min] = temp;
                }
            }
        }
    }
    public static void main(String[] args){
        int[] arrayBubbleSortNum = new int[20000]; // for Part 1
        int[] selectionSortNum = new int[20000];
        ArrayList<Integer> numArrayList = new ArrayList<>();
        String[] arrayBubbleSortString = new String[10000];
        String[] selectionSortString = new String[10000];
        ArrayList<String> stringArrayList = new ArrayList<>();
        try{
            BufferedReader reader = new BufferedReader(new FileReader("NumbersInFile.txt")); // for part 1
            BufferedReader reader2 = new BufferedReader(new FileReader("StringsInFile.txt")); // for part 2
            BufferedWriter writer = new BufferedWriter(new FileWriter("results.out")); // for part 1
            //BufferedWriter writerTest = new BufferedWriter(new FileWriter("Test.out")); // to test sort
            String line;
            String line2;
            int arrayIndexNum= 0;
            int arrayIndexString = 0;
            while((line = reader.readLine()) != null){
                int number = Integer.parseInt(line);//for part 1
                numArrayList.add(number); //for ArrayList for Numbers
                arrayBubbleSortNum[arrayIndexNum] = number;// for Bubble sort for Numbers
                selectionSortNum[arrayIndexNum]= number;// for Selection sort for Numbers
                arrayIndexNum++;//part 1
            }
            while((line2 = reader2.readLine()) != null){
                String text = line2;
                stringArrayList.add(line2);
                arrayBubbleSortString[arrayIndexString] = line2;
                selectionSortString[arrayIndexString] = line2;
                arrayIndexString++;
            }
            //selectionSort(selectionSortNum); // to test sort
            //writerTest.write(Arrays.toString(selectionSortNum)); // to test sort
            long startTimeBubbleNum = System.nanoTime();
            bubbleSort(arrayBubbleSortNum);
            long bubbleSortTimeNum = System.nanoTime() - startTimeBubbleNum; //Bubble sort Time
            long startTimeSelectionNum = System.nanoTime();
            selectionSort(selectionSortNum);
            long selectionSortTimeNum = System.nanoTime() - startTimeSelectionNum; //Selection Sort Time
            long startTimeArrayListNum = System.nanoTime();
            Collections.sort(numArrayList);
            long ArrayListSortTimeNum = System.nanoTime()-startTimeArrayListNum;// ArrayList Sort Time
            int arrayBubbleSortNumSize = arrayBubbleSortNum.length;
            writer.write("Jose Trevizo\nCS2050\nProgram6\n");
            writer.write("Number of Integers: " + arrayBubbleSortNumSize + "\n");
            writer.write("Bubble Sort Time for Integers: " + bubbleSortTimeNum + " NanoSeconds (nS)\n");
            writer.write("Selection Sort Time for Integers: " + selectionSortTimeNum + " NanoSeconds (nS)\n");
            writer.write("ArrayList Sort Time for Integers: " + ArrayListSortTimeNum + " NanoSeconds (nS)\n"); // end of part 1
            long startTimeBubbleString = System.nanoTime();
            bubbleSortString(arrayBubbleSortString);
            long bubbleSortTimeString = System.nanoTime() - startTimeBubbleString; //Bubble sort Time for Strings
            long startTimeSelectionString = System.nanoTime();
            selectionSortStrings(selectionSortString);
            long selectionSortTimeString = System.nanoTime() - startTimeSelectionString; //Selection sort time for Strings
            long ArrayListSortStartTimeString = System.nanoTime();
            Collections.sort(stringArrayList);
            long ArrayListSortTimeString = System.nanoTime() - ArrayListSortStartTimeString;//ArrayList Sort Time Strings
            int arrayBubbleSortStringSize = arrayBubbleSortString.length;
            writer.write("Number of Strings: " + arrayBubbleSortStringSize + "\n");
            writer.write("Bubble Sort Time for Strings: " + bubbleSortTimeString + " NanoSeconds (nS)\n");
            writer.write("Selection Sort Time for Strings: " + selectionSortTimeString + " NanoSeconds (nS)\n");
            writer.write("ArrayList Sort Time for Strings: " + ArrayListSortTimeString + " NanoSeconds (nS)"); // end for part 2
            reader.close();
            writer.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
