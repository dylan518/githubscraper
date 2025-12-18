package single_linkedList_ds_ques;

import java.util.List;

public class AddTwoNumbers {

	public static void main(String[] args) {
		int[] l1 = { 9, 9, 9, 9 };
		int[] l2 = { 9, 9, 9 };

		ListNode head1 = ListNode.arrayToLLConversion(l1);
		ListNode head2 = ListNode.arrayToLLConversion(l2);
		ListNode out = addTwoNumbers(head1, head2);
		System.out.println(out);
	}

	public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {

		ListNode t1 = l1;
		ListNode t2 = l2;

		ListNode dummyNode = new ListNode(-1);
		ListNode curr = dummyNode;
		int carry = 0;
		int sum = 0;
		while (t1 != null || t2 != null) {
			sum = carry;
			if (t1 != null) {
				sum = sum + t1.val;
			}
			if (t2 != null) {
				sum = sum + t2.val;
			}
			ListNode newNode = new ListNode(sum % 10);
			carry = sum / 10;
			curr.next = newNode;
			curr = curr.next;
			if (t1 != null)
				t1 = t1.next;
			if (t2 != null)
				t2 = t2.next;
		}

		// If there is a remaining carry after the loop, create a new node with the
		// carry
		if (carry != 0) {
			ListNode newNode = new ListNode(carry);
			curr.next = newNode;
		}

		return dummyNode.next;

	}

}
