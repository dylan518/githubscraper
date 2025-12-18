public class BinarySerach {
    public static int BinarySerach(int arr[],int key){
        int start = 0;
        int end = arr.length-1;

        while(start <= end){
            int mid = (start+end)/2;
            if(key ==arr[mid]){
                return mid;
            }else if(key > arr[mid]){
                start= mid+1;
            }else{
                end = mid-1;
            }

        }
        return -1;
    }

    public static void main(String args []){
        int array [] = {10,20,30,40,50,60,70,80,90,100};
        int item= 30;
        System.out.println("Element is present in : " + BinarySerach(array,item) );
    }
    
}
//time complexity O(log n)
// n > log n
//It gives a better peformance compared to the linear search.
