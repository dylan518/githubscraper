package org.alihmzyv.medium;

import org.alihmzyv.common.ListNode;

public class AddTwoNumbers {
    /**
     * My own solution. O(max(m, n))
     * @param l1
     * @param l2
     * @return
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0, null);
        ListNode node = head;
        int remainderFromPreviousSum = 0;
        while (!(l1 == null && l2 == null && remainderFromPreviousSum == 0)) {
            int sumOfDigits = remainderFromPreviousSum;
            if (l1 != null) {
                sumOfDigits += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sumOfDigits += l2.val;
                l2 = l2.next;
            }
            remainderFromPreviousSum = sumOfDigits / 10;
            node.next = new ListNode();
            node = node.next;
            node.val = sumOfDigits % 10;
        }
        return head.next;
    }

    public ListNode addTwoNumberV2(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0, null);
        ListNode node = dummyHead;
        int carry = 0;
        while (!(l1 == null && l2 == null && carry == 0)) {
            int digit1 = l1 == null ? 0 : l1.val;
            int digit2 = l2 == null ? 0 : l2.val;
            int sum = digit1 + digit2 + carry;
            carry = sum / 10;
            node.next = new ListNode(sum % 10);
            node = node.next;
            if (l1 != null)
                l1 = l1.next;
            if (l2 != null)
                l2 = l2.next;
        }
        return dummyHead.next;
    }
}
