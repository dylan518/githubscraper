public class binarySearch {
    public static void main(String[] args) {
        int[] nums = {-6,-3,-1,0,2,6,8,12,17};
        System.out.println(search(nums,0));
    }
    static int search(int[] arr, int target){
        int start =0;
        int end = arr.length-1;
        while(start<=end){
            int mid = start+(end-start)/2;
            if (target<arr[mid]){
                end = mid-1;
            } else if (target>arr[mid]) {   //arr[x] = gives value at index x
                start = mid+1;
            }else
            return mid;
        }
        return -1;
    }
}
