//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main(String[] args) throws IOException
	{
	        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while(t-->0)
        {
            int n = Integer.parseInt(br.readLine().trim());
            long a[] = new long[(int)(n)];
            // long getAnswer[] = new long[(int)(n)];
            String inputLine[] = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(inputLine[i]);
            }
            int k = Integer.parseInt(br.readLine().trim());
            
            Compute obj = new Compute();
            long answer[] = obj.printFirstNegativeInteger(a, n, k);
            int sz = answer.length;
            
            StringBuilder output = new StringBuilder();
            for(int i=0;i<sz;i++)
                output.append(answer[i]+" ");
            System.out.println(output);
            
        }
	}
}


// } Driver Code Ends


//User function Template for Java


class Compute {
    
    public long[] printFirstNegativeInteger(long A[], int N, int K)
    {
        int i = 0;
        int j = 0;
        long min = Long.MAX_VALUE;
        ArrayList<Long> arrayList = new ArrayList<>();
        Queue<Long> queue = new LinkedList<>();
        while(j<N){
            //calculations
            if(A[j] < 0){
                queue.offer(A[j]);
            }
            
            if(j - i + 1 < K){
                j++;
            } else if(j - i + 1 == K) {
               if(queue.isEmpty()){
                   arrayList.add(0L);
               } else {
                   arrayList.add(queue.peek());
                   if(A[i] == queue.peek()){
                       queue.poll();
                   }
               }
               i++;
               j++;
                
            }
            
        }
         long[] result = new long[arrayList.size()];
        for (int k = 0; k < arrayList.size(); k++) {
            result[k] = arrayList.get(k);
        }
        
        return result;
    }
}
