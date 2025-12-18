package com.mycompany.medianof2arrays;

public class ImprovedSolution {

    // 2 ms beat 59%. memory beat 58%
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1 == null || nums2 == null) throw new RuntimeException("inputs can not be null");
        int m = nums1.length;
        int n = nums2.length;

        if ((m == 0 && n==0 ) || m>1000 || n>1000) throw new RuntimeException("inputs out of range");

        int medianIndex=0, medianIndex2=0;

        if ((n+m) % 2 != 0) {
            medianIndex = (n + m) /2;
        } else {
            medianIndex2 = (n + m) /2;
            medianIndex = medianIndex2 - 1;
        }

        if (m == 0 ) {
            return getMedian(nums2, medianIndex, medianIndex2);
        }
        if (n == 0 ) {
            return getMedian(nums1, medianIndex, medianIndex2);
        }

        if (nums1[m-1] <= nums2[0]) return getMedianFrom2Arrays(nums1, nums2, medianIndex, medianIndex2);
        if (nums2[n-1] <= nums1[0]) return getMedianFrom2Arrays(nums2, nums1, medianIndex, medianIndex2);

        int index1 = 0, index2=0, count = 0;
        int[] merged = new int[2];
        double median;
        int targetCount = medianIndex2>medianIndex ? medianIndex2+1 : medianIndex+1;
        boolean singleMedian = medianIndex2<medianIndex;
        while (true) {
            if (nums1[index1] == nums2[index2]) {
                if (singleMedian) {
                    merged[0] = nums1[index1];
                } else {
                    merged[0] = merged[1];
                    merged[1] = nums1[index1];
                }
                index1 ++;
            } else if (nums1[index1] > nums2[index2]) {
                if (singleMedian) {
                    merged[0] = nums2[index2];
                } else {
                    merged[0] = merged[1];
                    merged[1] = nums2[index2];
                }
                index2++;
            } else {
                if (singleMedian) {
                    merged[0] = nums1[index1];
                } else {
                    merged[0] = merged[1];
                    merged[1] = nums1[index1];
                }
                index1++;
            }
            count ++;

            if (!singleMedian && medianIndex2 == count -1) {
                median = (double) (merged[0] + merged[1]) / 2;
                return median;
            } else if (singleMedian && medianIndex == count -1) {
                return merged[0];
            }

            if (index1==nums1.length) {
                for (int i=index2; i<nums2.length && count< targetCount; i++) {
                    if (singleMedian) {
                        merged[0] = nums2[i];
                    } else {
                        merged[0] = merged[1];
                        merged[1] = nums2[i];
                    }
                    count++;
                }
                if (singleMedian) {
                    median = merged[0];
                } else {
                    median = (double) (merged[0] + merged[1]) / 2;
                }
                return median;
            }

            if (index2==nums2.length) {
                for (int i=index1; i<nums1.length && count < targetCount; i++) {
                    if (singleMedian) {
                        merged[0] = nums1[i];
                    } else {
                        merged[0] = merged[1];
                        merged[1] = nums1[i];
                    }
                    count++;
                }
                if (singleMedian) {
                    median = merged[0];
                } else {
                    median = (double) (merged[0] + merged[1]) / 2;
                }
                return median;
            }
        }
    }

    private double getMedianFrom2Arrays(int[] numsSmall, int[] numsBig, int medianIndex, int medianIndex2) {
        double result;

        if (medianIndex == numsSmall.length-1) {
            if (medianIndex2 > medianIndex) {
                result = (double) (numsSmall[medianIndex] + numsBig[medianIndex2-numsSmall.length]) / 2;
            } else {
                result = numsSmall[medianIndex];
            }
        } else if (medianIndex < numsSmall.length-1) {
            result = getMedian(numsSmall, medianIndex, medianIndex2);
        } else {
            result = getMedian(numsBig, medianIndex-numsSmall.length, medianIndex2-numsSmall.length);
        }

        return result;
    }

    private double getMedian(int[] nums, int medianIndex, int medianIndex2) {
        double result;
        if (medianIndex2 > medianIndex) {
            result = (double) (nums[medianIndex] + nums[medianIndex2]) / 2;
        } else {
            result = nums[medianIndex];
        }
        return result;
    }
}
