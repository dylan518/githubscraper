package com.dsa.starproblems;

import java.util.ArrayList;
import java.util.List;

public class Subsets {
    public static void main(String[] args) {
        Subsets subsets = new Subsets();
        System.out.println(subsets.subsets2(new int []{1,2,3}));
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
       for(int i=0;i< 1<<nums.length;i++){
           List<Integer> list= new ArrayList<>();
           for(int j=0;j<nums.length;j++){
               if (((1 << j) & i) != 0) {
                   list.add(nums[j]);
               }
           }
           result.add(list);
       }
       return result;
    }

    public List<List<Integer>> subsets2(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result,new ArrayList<>(),nums,0);
        return result;
    }

    public void backtrack(List<List<Integer>> result,List<Integer> list,int[] nums,int start){
        result.add(new ArrayList<>(list));
        for(int i=start;i<nums.length;i++){
            list.add(nums[i]);
            backtrack(result, list, nums,i+1);
            list.remove(list.size()-1);
        }
    }
}
