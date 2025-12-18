//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GfG
{
    public static void main (String[] args)
    {
        
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int n = sc.nextInt();
            String arr[] = new String[n];
            
            for(int i = 0; i < n; i++)
                arr[i] = sc.next();
            
            Solution obj = new Solution();    
            String result[] = obj.winner(arr, n);
            System.out.println(result[0] + " " + result[1]);
            
           
        }
        
    }
}

// } Driver Code Ends


//User function Template for Java


class Solution
{
    //Function to return the name of candidate that received maximum votes.
    public static String[] winner(String arr[], int n)
    {
        // add your code
        HashMap<String, Integer> hs = new HashMap<>();
        for(String s : arr){
            hs.put(s, hs.getOrDefault(s,0)+1);
        }
        
        int maxVote = 0;
        String name = "";
        for(String entry : hs.keySet()){
            if(hs.get(entry) > maxVote){
                maxVote = hs.get(entry);
                name = entry;
            }
            
            if(hs.get(entry) == maxVote){
                if(entry.compareTo(name) < 0){
                    name = entry;
                }
            }
        }
        return new String[]{name,Integer.toString(maxVote)};
    }
}

