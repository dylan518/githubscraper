package Lec23;

import java.util.*;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        next = null;
    }
}

public class RemoveN {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Node head = null;
        Node tail = null;

        int n = sc.nextInt();
        int p=n;
        int k = sc.nextInt();
        while (n-- > 0) {
            int data =sc.nextInt();
            Node newNode = new Node(data);
            if (head == null) {
                head = newNode;
                tail = newNode;
            } else {
                tail.next = newNode;
                tail = newNode;
            }
           
        }

        // int k = sc.nextInt();
        int result = findKthFromLast(head, k,p);
        // System.out.println();
        // System.out.println(result);
     
    }

    public static int findKthFromLast(Node head, int k, int n) {
        Node slow = head;
        Node fast = head;
        fast = fast.next;
        if (n==k) {
            Node temp=head;
            Node temp2=temp.next;
    
    temp.next=temp2;
    head=temp.next;
    display(head);
            
        }
        
       
        else{

        
        for (int i = 0; i < k-1; i++) {
            if (fast == null) {
                return -1; // k is greater than the length of the linked list
            }
            fast = fast.next;
        }

        while (fast != null && fast.next!=null ){
            slow = slow.next;
            fast = fast.next;
        }
        Node temp2=slow.next.next;

slow.next=temp2;
display(head);}
    
        return slow.data;
    }
    public static void display(Node head) {
    
    Node temp=head;
    while (temp!=null) {
        System.out.print(temp.data+"  ");
        temp=temp.next;
        
    }
    // System.out.println("null");
    
}
}