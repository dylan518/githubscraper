package advance.day_20_1D_Array.assignment;

public class Max_Sum_Contiguous_Subarray {

    // Using Kadane's algo we can find it in linear time
    public static int maxSubArray(final int[] A) {

        int ans = A[0];
        int sum = 0;

        for (int i = 0;i<A.length;i++)
        {
            sum += A[i];
            ans = Math.max(ans,sum);
            //Reset sum as no point in carrying it further
            if( sum < 0)
                sum = 0;
        }
        return ans;
    }

    public static void main(String[] args) {

        System.out.println(maxSubArray(new int[]{1, 2, 3, 4, -10}));
        System.out.println(maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
    }
}
