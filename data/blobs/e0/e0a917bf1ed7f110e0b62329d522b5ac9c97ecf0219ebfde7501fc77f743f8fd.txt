import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Twosum{
    public static void main(String[] args) {
       int arr[]={1,2,4,5,6,7};
        int target=11;
        Map<Integer,Integer> m=new HashMap<>();
        int n=3;


        int arr2[]= new int[n*2];

        for(int i=0;i<n;i++){
            arr2[i*2]=arr[i];
            arr2[i*2+1]=arr[i+n];
        }

        System.out.println(Arrays.toString(arr2));
        
        for(int i=0;i<arr.length;i++){
            int comp=target-arr[i];
            if(m.containsKey(comp)){
                int result[]={m.get(comp),i};
                System.out.println(Arrays.toString(result));
            }
            else{
                m.put(arr[i],i);
            }


        }
        
    }
}