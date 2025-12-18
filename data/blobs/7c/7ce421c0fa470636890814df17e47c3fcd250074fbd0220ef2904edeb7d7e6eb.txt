/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

/*
 * Binary Search (Left Bound)
 * 
 * O(log(n)) time | O(1) space
 * 
 * 2022/11/11
 */
class Solution278 {
    // This is the dummy function to fix the syntax, the actual function is from the API!
    private boolean isBadVersion(int n) {
        return true;
    }

    public int firstBadVersion(int n) {
        int left = 0;
        int right = n - 1;
        int mid;
        while (left <= right) {
            mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}