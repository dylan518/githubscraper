package _28thDecQuestions;

import java.util.*;

public class DetectCycleInLL {
	
	public static void main(String[] args) {
		
		Node head = new Node(1);
		head.next = new Node(2);
		head.next.next = new Node(3);
		head.next.next.next = new Node(4);
		head.next.next.next.next = head;
		
		System.out.println(detectCycle(head));
		
	}

	private static boolean detectCycle(Node head) {
		Node slow = head;
		Node fast = head;
		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
			if(slow == fast) {
				return true;
			}
		}
		
		return false;
		
		
	}

}
