package DSA.Problem03;

public class solution {
    public static void main(String[] args) {
        int[] arr = {8,4,2};
        int n = arr.length;
        System.out.println(isPossible(arr,n));
    }

    public static boolean isPossible(int[] arr, int n) {
        if(n==1 || n==2) return true;
        int counter = 0;
        for(int i=1;i<n;i++) {
           if(arr[i-1]>arr[i]){
               if(counter==1) return false;
               counter++;
               if(i>2 && arr[i]>arr[i-2]){
                   arr[i-1]=arr[i];
               } else {
                   arr[i]=arr[i-1];
               }
           }
        }
        return true;
    }
}

