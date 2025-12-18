
class Solution
{
    //Function to rotate an array by d elements in counter-clockwise direction. 
    static void rotateArr(int arr[], int k, int n)
    {
        // add your code here
        if(k > n){
            k = k % n;
        }
        reverse(arr , 0 , k - 1);
        reverse(arr , k , n - 1);
        reverse(arr, 0 , n - 1);
    }
    
   public static void reverse(int[] arr ,int low , int high){
        while(low <= high){
            int temp = arr[low];
            arr[low] = arr[high];
            arr[high] = temp;
            low++;
            high--;
        }
    }
}