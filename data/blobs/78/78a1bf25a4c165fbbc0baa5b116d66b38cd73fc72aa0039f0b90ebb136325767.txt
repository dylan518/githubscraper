// { Driver Code Starts
import java.util.*;
import java.io.*;
import java.lang.*;

class GFG
{
    public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
		while(t-->0){
		    
		    int n = Integer.parseInt(br.readLine().trim());
		    String inputLine[] = br.readLine().trim().split(" ");
		    int arr[] = new int[n];
		    for(int i=0; i<n; i++){
		        arr[i] = Integer.parseInt(inputLine[i]);
		    }
		    
		    int k = Integer.parseInt(br.readLine().trim());
		    
		    Solution ob= new Solution();
		    System.out.println(ob.countKdivPairs(arr, n, k));
		}
	}
}// } Driver Code Ends


//User function Template for Java

class Solution
{
    public static long countKdivPairs(int arr[], int n, int k)
    {
        //code here
        long count=0;
        int a[]=new int[k];
        for(int i=0;i<n;i++){
            a[arr[i]%k]++;
        }
        count+=((a[0]*(a[0]-1))/2);
       
        for(int i=1;i<=k/2&&(i!=k-i);i++){
            count+=((a[i])*(a[k-i]));
        }
         if((k%2)==0){
            count+=(a[k/2]*(a[k/2]-1)/2);
        }
        return count;
    }
}