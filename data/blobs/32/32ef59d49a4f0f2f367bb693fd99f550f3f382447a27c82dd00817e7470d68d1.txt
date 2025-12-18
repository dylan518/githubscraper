class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1 == null || nums2 == null)
           return 0;
        
        int n = nums1.length;
        int m = nums2.length;

        if (n > m) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int mid = (n + m) / 2;

        if (n == 0) {
            return (m % 2 == 0)? (nums2[mid - 1] + nums2[mid]) / 2.0 : (double) nums2[mid];
        }
        
        int nums1Mid = n / 2;
        int nums2Mid = mid - nums1Mid - 1;

        while (nums1Mid >= 0 &&  nums2Mid < (m - 1) && nums1[nums1Mid] > nums2[nums2Mid + 1]) {
            nums1Mid --;
            nums2Mid ++;
        }

        while (nums2Mid >= 0 &&  nums1Mid < (n - 1) && nums2[nums2Mid] > nums1[nums1Mid + 1]) {
            nums1Mid ++;
            nums2Mid --;
        }

        if ((n + m) % 2 == 0) {
            int ele = 0;
            if (nums1Mid == -1) {
                return (nums2[nums2Mid] + nums2[nums2Mid - 1]) / 2.0;
            }
            if (nums2Mid == -1) {
                return (nums1[nums1Mid] + nums1[nums1Mid - 1]) / 2.0;
            }
            if (nums1[nums1Mid] > nums2[nums2Mid]) {
                ele += nums1[nums1Mid];
                if (nums1Mid > 0){
                    ele += Math.max(nums1[nums1Mid - 1], nums2[nums2Mid]);
                }
                else {
                    ele += nums2[nums2Mid];
                }
            }
            else {
                ele += nums2[nums2Mid];
                if (nums2Mid > 0){
                    ele += Math.max(nums1[nums1Mid], nums2[nums2Mid - 1]);
                }
                else {
                    ele += nums1[nums1Mid];
                }
            }
            return ele / 2.0;
        }
        if (nums1Mid == -1)
            return nums2[nums2Mid];
        if (nums2Mid == -1)
            return nums1[nums1Mid];
        return Math.max(nums1[nums1Mid], nums2[nums2Mid]);
        
    }
}