package easy;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import DataStructs.ListNode;

public class ReverseLinkedListTest {

    @Test
    public void testReverseList() {
        ReverseLinkedList reverseLinkedList = new ReverseLinkedList();

        // Test Case 1: Normal case with multiple elements
        ListNode head1 = createList(new int[]{1, 2, 3, 4, 5});
        ListNode reversed1 = reverseLinkedList.reverseList(head1);
        assertEquals("5->4->3->2->1", listToString(reversed1));

        // Test Case 2: List with a single element
        ListNode head2 = createList(new int[]{1});
        ListNode reversed2 = reverseLinkedList.reverseList(head2);
        assertEquals("1", listToString(reversed2));

        // Test Case 3: Empty list
        ListNode head3 = null;
        ListNode reversed3 = reverseLinkedList.reverseList(head3);
        assertEquals("", listToString(reversed3));

        // Test Case 4: List with duplicate elements
        ListNode head4 = createList(new int[]{1, 1, 1, 1});
        ListNode reversed4 = reverseLinkedList.reverseList(head4);
        assertEquals("1->1->1->1", listToString(reversed4));

        // Test Case 5: List with consecutive elements
        ListNode head5 = createList(new int[]{10, 20, 30});
        ListNode reversed5 = reverseLinkedList.reverseList(head5);
        assertEquals("30->20->10", listToString(reversed5));
    }

    // Helper method to create a linked list from an array
    private ListNode createList(int[] values) {
        if (values.length == 0) return null;
        ListNode head = new ListNode(values[0]);
        ListNode current = head;
        for (int i = 1; i < values.length; i++) {
            current.next = new ListNode(values[i]);
            current = current.next;
        }
        return head;
    }

    // Helper method to convert a linked list to a string for easy comparison
    private String listToString(ListNode head) {
        StringBuilder sb = new StringBuilder();
        while (head != null) {
            if (sb.length() > 0) sb.append("->");
            sb.append(head.val);
            head = head.next;
        }
        return sb.toString();
    }
}
