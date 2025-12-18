import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class continuousmedian {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //read number of testcases T
        int T = Integer.parseInt(input.nextLine());
        //loop through T times
        for(int i = 0; i < T; i++){
            //read no. of input N
            int N = Integer.parseInt(input.nextLine());
            //create ArrayList A
            ArrayList<Long> A = new ArrayList<>(N);
            //create long sum
            long sum = 0;
            //while there's more elements
            for(int x = 0; x < N; x++) {
                //read element
                //add to A
                A.add(input.nextLong());
                //sort Array
                Collections.sort(A);
                //get median ~~~
                long median = getMedian(A);
                //add median to sum
                sum += median;
            }
            //after no more elements print sum.
            System.out.println(sum);
            //read next line
            input.nextLine();
        }

        /*Get median*/
        //When N is odd, median is clearly defined. Middle element of sorted array.
        //However when N is even the median is the average of the two middle values, rounded down so that we always have an integer median.
    }

    //create method called getMedian, takes a sorted Array input and returns middle element if odd, or rounded down average of the middle 2 if even
    //returns int
    public static long getMedian(ArrayList<Long> A) {

        long median;
        int length = A.size();

        //Even
        if(length % 2 == 0 ){
            median = (A.get((length/2) - 1) + A.get(length/2))/2;
        }

        //odd
        else{
            median = A.get(length/2);
        }

        return median;
    }


    public static void insertion_sort(ArrayList<Long> arr){
        int n = arr.size();

        for(int i = n-1; i < n; i++){
            long key = arr.get(i);
            int j = i-1;
            while(j>=0 && (arr.get(j) > key)){
                arr.set(j+1, arr.get(j));
                j--;
            }
            arr.set(j+1, key);
        }
    }
    /*
    Insertion Sort

    First element is sorted
    for each unsorted element X
        extract element X
        for lastSortedIndex down to 0
            if lastSortedIndex > X
                push that index up
            break loop and insert X
     */

}
