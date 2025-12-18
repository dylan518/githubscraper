public class LeetCode_141 {
    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    public class Solution {
        public boolean hasCycle(ListNode head) {
            if (head == null)
                return false;
            ListNode index = head;
            while (index.next != null) {
                if (index.val == Integer.MIN_VALUE)
                    return true;
                index.val = Integer.MIN_VALUE;
                index = index.next;
            }
            return false;
        }
    }
}
