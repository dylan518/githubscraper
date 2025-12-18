/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    private ListNode left;
    public boolean isPalindrome(ListNode head) {
        left = head; // Initialize left to the head of the list
        return checkPalindrome(head);
    
    }
        private boolean checkPalindrome(ListNode right) {
        if (right == null) {
            return true;
        }
        boolean isPal = checkPalindrome(right.next);
        if (!isPal) {
            return false;
        }
        boolean isEqual = (left.val == right.val);
        left = left.next;
        return isEqual;
    }
}
