package com.ysk.leetcode.queue;

import java.util.*;
import java.util.concurrent.ConcurrentLinkedQueue;

/**
 * 239. 滑动窗口最大值
 * 思路：如何减少匹配次数？
 */
public class MaxSlidingWindow {

    /**
     * 暴力解法
     *
     * @param nums
     * @param k
     * @return
     */
    public static int[] maxSlidingWindow(int[] nums, int k) {

        int[] result = new int[nums.length - k + 1];

        //窗口的元素
        int leftIndex = 0;
        int rightIndex = k - 1;
        for (; rightIndex < nums.length; leftIndex++, rightIndex++) {
            result[leftIndex] = max(nums, leftIndex, rightIndex);
        }

        return result;
    }

    private static int max(int[] nums, int left, int right) {
        int max = Integer.MIN_VALUE;
        while (left <= right) {
            max = Math.max(max, nums[left]);
            left++;
        }

        return max;
    }

    /**
     * 使用单调递增队列，在头部维护窗口最大值
     *
     * @param nums
     * @param k
     * @return
     */
    public static int[] maxSlidingWindow2(int[] nums, int k) {
        int[] result = new int[nums.length - k + 1];
        Deque<Integer> deque = new LinkedList<>();
        //加入K长度的内容
        for (int i = 0; i < k; i++) {
            add(nums[i], deque);
        }
        //头部元素为最大的元素
        result[0] = deque.peek();
        int size = 1;
        for (int i = k; i < nums.length; i++) {
            //移除前一个元素
            poll(nums[i - k], deque);
            //加入当前元素
            add(nums[i], deque);
            //加入最大值
            result[size] = deque.peek();
            size++;
        }
        return result;
    }

    /**
     * 保持单调递减，如果添加的元素比上一个元素大，就弹出上个元素
     * 只保留可能最大的数据
     *
     * @param num
     * @param deque
     */
    private static void add(int num, Deque<Integer> deque) {
        while (!deque.isEmpty() && num > deque.getLast()) {
            deque.removeLast();
        }
        deque.add(num);
    }

    /**
     * 弹出元素时，比较当前要弹出的数值是否等于队列出口的数值，如果相等则弹出
     *
     * @param num
     * @param deque
     */
    private static void poll(int num, Deque<Integer> deque) {
        if (!deque.isEmpty() && num == deque.peek()) {
            deque.poll();
        }
    }


}
