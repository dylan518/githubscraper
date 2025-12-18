import java.util.Scanner;

public class problem7 {
    public static void run() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] array = new int[n];
        for(int i=0; i<n; i++){
            array[i]=sc.nextInt();
        }
        System.out.print("result: ");
        long startTime = System.nanoTime();
        reverseArr(array, n-1);
        double runtime = (double)(System.nanoTime() - startTime)/1000000000;
        System.out.println("runtime: "+runtime + "\ntime complexity: O(n)");
    }

    /**
     * this method prints the given array in the reverse order
     * it uses a recursive approach
     * time complexity: O(n), where n is the size of the array
     * the method iterates through numbers from n to 0,
     * resulting in linear time complexity
     *
     * @param array the given array
     * @param index the index of the element being printed
     */
    public static void reverseArr(int[] array, int index){
        System.out.print(array[index]+" ");
        if (index>0){
            reverseArr(array,index-1);
        }
    }
}
