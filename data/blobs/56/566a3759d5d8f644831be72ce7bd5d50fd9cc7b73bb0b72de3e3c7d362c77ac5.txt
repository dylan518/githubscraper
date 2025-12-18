package LINKED_LIST;

public class PrintUsingRecursion {
    public static void PrintRecursively(Node head){
        if(head == null) return;
        PrintRecursively(head.next);  // reverse case
        System.out.println(head.val);
        //PrintRecursively(head.next);  // normal case


    }
    public static void main(String[] args){
        Node a=new Node(34);
        Node b=new Node(45);
        Node c=new Node(12);
        Node d=new Node(90);
        Node e=new Node(56);
        a.next=b;
        b.next=c;
        c.next=d;
        d.next=e;
        PrintRecursively(a);


    }
}
