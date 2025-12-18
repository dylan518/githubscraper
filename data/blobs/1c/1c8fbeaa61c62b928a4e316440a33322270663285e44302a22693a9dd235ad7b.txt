package dsa.with.shagun.scaler.advance.Hashing.session1;

import java.util.HashSet;

public class LongestSeq {
    public static void main(String[] args) {
        System.out.println(longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));
        System.out.println(longestConsecutive(new int[]{2, 1}));
    }

    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public static int longestConsecutive(final int[] A) {


        //approach 1 :  Sort Elements, Iterate over array to check max. len of seq with difference in each element as 1
        //TC : O(nlong),SC:O(1)

        //approach 2 : Using Hashset if we have duplicates else hashmap
        // since we are not using sorting we will check whether next element is present in hm/hs or not if it is present we will keep on traversing till next element is present
        // But this approach can take O(n2) if we have elements in sorted order.
        //OPTIMISATION : Don't  check for subsequence if smaller element exists.ONLY CHECK SUBSEQ LENGTH FOR ELEMENTS WHOSE SMALLER ELEMENT IS NOT PRESENT
        //TC :O(N), SC:O(N)

        HashSet<Integer> hs = new HashSet<Integer>();
        int maxLenSubseq = 0;
        int count = 0;

        //insert all elements in hashset
        for (int i = 0; i < A.length; i++) {
            hs.add(A[i]);
        }

        // iterate for all elements in array
        for (int x : A) {
            //check length of subsequence if there exists NO smaller element in hashset
            if (!hs.contains(x - 1)) {
                count = 1;
                int nextEle = x + 1;
                while (hs.contains(nextEle)) { // if adjacentelement exists increment count and increment i
                    count++;
                    nextEle++;
                }
            }
            maxLenSubseq = Math.max(maxLenSubseq, count);
        }
        return maxLenSubseq;
    }
}
