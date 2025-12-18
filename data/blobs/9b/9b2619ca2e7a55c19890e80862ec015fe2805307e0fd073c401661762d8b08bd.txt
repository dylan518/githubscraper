package com.ibrahim.dsa.day5;

import java.util.*;

public class RemoveNthNodeFromBackOfLinkedList01 {
	public ListNode removeNthFromEnd(ListNode head, int n) {
		ListNode start = new ListNode();
		start.next = head;
		ListNode fast = start;
		ListNode slow = start;

		for (int i = 1; i <= n; ++i)
			fast = fast.next;

		while (fast.next != null) {
			fast = fast.next;
			slow = slow.next;
		}

		slow.next = slow.next.next;

		return start.next;
	}
}
/*
 * Time Complexity: O(N)
 * 
 * Space Complexity: O(1)
 */
