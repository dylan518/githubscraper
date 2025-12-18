import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();  // Read array size
        int[] arr = new int[N];  // Input array 
        
        // Read the array values
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }

        // Track presence of numbers 0..N in the array
        boolean[] present = new boolean[N + 1];
        // Count frequency of numbers 0..N in the array
        int[] frequency = new int[N + 1];

        // Populate presence and frequency arrays
        for (int num : arr) {
            // Only numbers ≤ N affect mex calculation for 0..N
            if (num <= N) {
                present[num] = true;  // Mark number as present
                frequency[num]++;     // Increment its count
            }
        }

        // Calculate prefix[i] = number of missing elements in 0..i-1
        int[] prefix = new int[N + 2];  // Extra space for mex = N+1
        prefix[0] = 0;  // Base case: no elements needed for mex 0
        
        // Build prefix array to track cumulative missing elements
        for (int i = 1; i <= N + 1; i++) {
            // prefix[i] = prefix[i-1] + (1 if i-1 is missing, else 0)
            prefix[i] = prefix[i - 1] + (present[i - 1] ? 0 : 1);
        }

        // Calculate minimum operations for each mex value 0..N
        for (int i = 0; i <= N; i++) {
            // Operations needed to ensure all 0..i-1 are present
            int missing = prefix[i];
            // Operations needed to remove all instances of i
            int cnt = frequency[i];
            
            // Final cost is max of these two requirements
            System.out.println(Math.max(missing, cnt));
        }
    }
}