package Questions.two_pointer.Sliding_window;
import java.util.*;

public class count_distinct_element_in_window {
    
    public static ArrayList<Integer> count(int[] arr,int N,int B){
        int i=0;
        int j=0;
        HashMap<Integer,Integer> map=new HashMap<>();
        ArrayList<Integer> ans=new ArrayList<>();

        while(j<N){
            if(!map.containsKey(arr[j])){
                map.put(arr[j],1);
            }
            else{
                map.put(arr[j],map.get(arr[j])+1);
            }
            if(j-i+1<B){
                j++;
            }
            else if(j-i+1==B){
                ans.add(map.size());
                int put=map.get(arr[i])-1;
                if(put==0){
                    map.remove(arr[i]);
                }
                else{
                    map.put(arr[i],put);
                }
                i++;
                j++;
            }
        }
        return(ans);
    }

    public static void main(String[] args){
        int[] arr={1 ,2, 1 ,3 ,4 ,3};
        ArrayList<Integer> ans=count(arr, 6, 3);
        for(int i=0;i<ans.size();i++){
            System.out.print(ans.get(i)+" ");
        }

    }
}
