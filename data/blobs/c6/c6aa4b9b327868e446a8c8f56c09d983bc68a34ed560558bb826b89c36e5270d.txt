public class ReversalLinkedlist {
    class Node{
        int data;
        Node next;
        Node(int d)
        {
            data=d;
            next = null;
        }
    }
    Node head;
    public void insertAtEnd(int newData)
    {
        Node newNode =new Node(newData);
        if(head==null)
        {
            head = newNode;
            return ;
        }
        Node curr=head;
        while(curr.next!=null)
        {
            curr=curr.next;
        }
        curr.next=newNode;
    }
    public void printList()
    {
        if(head==null)
        {
            System.out.println("LinkedList is empyt");
            return;
        }
        Node temp = head;
        while(temp != null )
        {
            System.out.print(temp.data+"->");
            temp = temp.next;
        }
    }
    public void reverse()
    {
        Node curr=head;
        Node prev=null;
        Node next=null;
        while(curr!=null)
        {
            next=curr.next;
            curr.next=prev;
            prev=curr;
            curr=next;
        }
        head =prev;
    }
    public void middleList()
    {
        if(head==null)
        {
            System.out.println("list is empty");
            return ;
        }
        Node slow=head;
        Node fast=head;
        while (fast!=null && fast.next!=null) {
            slow=slow.next;
            fast=fast.next.next;
        }
        System.out.println("The middle ele:"+slow.data);
    }
    public void detectLoop()
    {
        if(head==null)
        {
            return ;
        }
        int flag=0;
        Node slow=head;
        Node fast=head;
        while (slow!=null && fast!=null &&fast.next!=null) {
            slow=slow.next;
            fast=fast.next.next;
            if(slow==fast)
            {
                flag=1;
                return ;
            }
        }
        if(flag==1)
        {
            System.out.println("There is a loop in the list");
        }
        else{
            System.out.println("No Loop is detected");
        }
    }
    public static void main(String[] args) {
        ReversalLinkedlist l=new ReversalLinkedlist();
        l.insertAtEnd(2);
        l.insertAtEnd(5);
        l.insertAtEnd(7);
        l.insertAtEnd(9);
        l.insertAtEnd(13);
        l.insertAtEnd(21);
        l.printList();
        System.out.println();
        l.reverse();
        System.out.println("Reverse Linked list: ");
        l.printList();
        System.out.println();
        l.middleList();
        Node temp=l.head;
        while (temp.next!=null) {
            temp=temp.next;
        }
        temp.next=l.head;
        System.out.println();
        l.detectLoop();
    }
}
