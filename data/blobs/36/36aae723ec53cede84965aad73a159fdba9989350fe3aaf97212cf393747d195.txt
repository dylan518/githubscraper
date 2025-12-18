package search;

public class Demo793 {

    public int preimageSizeFZF(int K) {
        // + 1
        return (int)(right_bound(K) - left_bound(K) + 1);
    }

    public Long left_bound(int target){
        long left = 0;
        long right = Long.MAX_VALUE;
        while (left<=right){
            long mid = left+ (right-left)/2;
            if(trailingZeroes(mid)<=target){
                left = mid+1;
            }else {
                right = mid-1;
            }
        }
        return left;
    }

    public Long right_bound(int target){
        long left = 0;
        long right = Long.MAX_VALUE;
        while (left<right){
            long mid = left+ (right-left)/2;
            if(trailingZeroes(mid)<=target){
                left = mid+1;
            }else {
                right = mid;
            }
        }
        return left-1;
    }



    public long trailingZeroes(long n){
        int count = 0;
        int divider = 5;
        while (divider<n){
            count += n/divider;
            divider *= 5;
        }
        return count;
    }
}
