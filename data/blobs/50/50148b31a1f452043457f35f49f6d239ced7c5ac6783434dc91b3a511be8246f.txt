import java.util.*;

class nthnodedellast {
    public static class node {
        int data;
        node next;

        node(int data) {
            count++;
            this.data = data;
            this.next = null;
        }
    }

    static node head;
    static node tail;
    static int count = 0;

    void lastadd(int data) {
        node newnode = new node(data);
        if (head == null) {
            head = newnode;
            tail = newnode;
        } else {
            tail.next = newnode;
            tail = newnode;

        }

    }

    public static void finddel(int k) {
        node n = head;
        int num = count - k - 1;
        int x = 0;
        if(k==count){
            head=head.next;
            return;
        }
        while (x != num) {
            n = n.next;
            x++;
        }
        n.next = n.next.next;

    }

    public static void print() {
        node n = head;
        System.out.println("Data :");
        while (n != null) {
            System.out.println(n.data);
            n = n.next;

        }

    }

    public static void main(String args[]) {
        nthnodedellast list = new nthnodedellast();
        System.out.println("Enter Size :\n");
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        System.out.println("Enter Data :\n");
        for (int i = 0; i < size; i++) {
            list.lastadd(sc.nextInt());
        }
        list.print();
        System.out.println("Enter node number:");
        int n = sc.nextInt();
        finddel(n);
        print();
    }

}