package huaweiC100;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
//有问题

public class HW47 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String source = in.next();
        int target = in.nextInt();
        String substring = source.substring(1, source.length() - 1);
        String[] split = substring.split(",");
        int arr[]=new int[split.length];
        for (int i = 0; i < split.length; i++) {
            arr[i]=Integer.valueOf(split[i]);
        }
        Map<Integer,Integer> map=new HashMap<>();
        int IndexSum=Integer.MAX_VALUE;
        int a=-1;
        int b=-1;
        for (int i = 0; i < arr.length; i++) {
            if(map.containsKey(target-arr[i])){
                int currentIndexSum=i+map.get(target-arr[i]);
                if(currentIndexSum<IndexSum){
                     IndexSum=currentIndexSum;
                    a=target-arr[i];
                    b=arr[i];
                }

            }else {
                map.put(arr[i],i);
            }
        }
        System.out.print("[");
        System.out.print(a+",");
        System.out.print(b+"]");
    }
}
