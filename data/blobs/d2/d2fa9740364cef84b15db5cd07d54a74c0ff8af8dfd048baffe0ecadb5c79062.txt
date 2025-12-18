package Recursion;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
//get All unique comb
public class subSetSum2 {
    public static void main(String[] args) {
        List<List<Integer>> res=new ArrayList<>();
        List<Integer> ds=new ArrayList<>();
        int[] arr={1,2,2};
        Arrays.sort(arr);
        getAllUniqueSubsets(arr,res,ds,0);

        System.out.println(res);
    }

    private static void getAllUniqueSubsets(int[] arr, List<List<Integer>> res, List<Integer> ds, int n) {
        res.add(new ArrayList<>(ds));
        for(int i=n;i<arr.length;i++){
            if(i!=n && arr[i]==arr[i-1])continue;
            ds.add(arr[i]);
            getAllUniqueSubsets(arr,res,ds,n+1);
            ds.remove(ds.size()-1);
        }
    }
}
