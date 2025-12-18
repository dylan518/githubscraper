//{ Driver Code Starts

// Initial Template for Java
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int N = sc.nextInt();
            ArrayList<Integer> arr = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                arr.add(sc.nextInt());
            }
            Solution ob = new Solution();

            ArrayList<Integer> ans = ob.subsetSums(arr, N);
            Collections.sort(ans);
            for (int sum : ans) {
                System.out.print(sum + " ");
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends


// User function Template for Java//User function Template for Java
class Solution {
    public void subsetsum(ArrayList<Integer> arr, int n, int ind,int sum, ArrayList<Integer> subset ){
        // ArrayList<Integer> subset=new ArrayList<>();
        if(ind==n){
            subset.add(sum);
            return;
        }
        subsetsum(arr,n, ind+1,sum+arr.get(ind),subset);
        subsetsum(arr, n,ind+1,sum,subset);
        
        
    }
    ArrayList<Integer> subsetSums(ArrayList<Integer> arr, int n) {
       
        // code here
        ArrayList<Integer> subset=new ArrayList<>();
        subsetsum(arr,n,0,0,subset);
        Collections.sort(subset);
        return subset;
    }
}