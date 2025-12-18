package me.motyim.training;

public class MyLinkedList {

    Node head ;

    class Node {
        int data;
        Node next , prev ;

        Node(int data){
            this.data = data;
            this.next= this.prev = null;
        }
    }

    public static void main(String[] args) {
        MyLinkedList list = new MyLinkedList();

        list.push(7);
        list.push(6);
        list.push(5);
        list.push(4);
        list.push(3);
        list.push(2);
        list.push(1);

        System.out.println("Given Linked List ");
        list.printList();

        /* Convert List to BST */
        Node root = list.sortedListToBST();
        System.out.println("");
    }

    private Node sortedListToBST() {
        /*Count the number of nodes in Linked List */
        int n = countNodes();
        return sortedListToBSTRecur(n);
    }

    private Node sortedListToBSTRecur(int n) {

        if(n<= 0) return null;

        Node left = sortedListToBSTRecur(n/2);
        Node root = head;
        root.prev = left;
        head = head.next;
        root.next = sortedListToBSTRecur(n-n/2-1);
        return root;
    }

    private int countNodes() {
        int count = 0 ;
        Node itr = head;
        while(itr != null ){
            count++;
            itr = itr.next;
        }
        return count;
    }

    private void printList() {
        Node itr = head ;
        while(itr !=null){
            System.out.print(itr.data + " ");
            itr = itr.next;
        }
    }

    private void push(int i) {
        Node node = new Node(i);
        node.prev=null;
        node.next=head;

        if(head !=null)
            head.prev = node;

        head = node;
    }
}
