package Recursion;
import java.util.*;
public class CombinationSum {
    public static void main(String[] args) {
        ArrayList<Integer> oldArr  = new ArrayList<Integer>();
        oldArr.add(2);
        oldArr.add(3);
        oldArr.add(6);
        oldArr.add(7);
        ArrayList<Integer> newArr = new ArrayList<Integer>();
        int target = 7;
        int index = 0;
        combination(oldArr,newArr,target,index);
    }
    
    static void combination(ArrayList<Integer>oldArr,ArrayList<Integer> newArr, int target , int index){
   if(index==oldArr.size()){
       if(target==0){
           System.out.println(newArr);
       }
       return;
   }
   if(oldArr.get(index)<=target){
       newArr.add(oldArr.get(index));
       combination(oldArr,newArr,target- oldArr.get(index), index);
       newArr.remove(oldArr.get(index));
   }

   combination(oldArr,newArr,target, index+1);
    }
}
