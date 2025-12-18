import java.util.Scanner;

public class Nodee {
    //Linked List
     int data;
    Nodee link;
    Nodee(int data){
        this.data=data;
    }
    static Nodee head=null;
    //Inserting
    public static void insert(int elment){
        Nodee temp=new Nodee(elment);
        if(head==null){
            head=temp;
        }
        else{
            Nodee ptr=head;
            while(ptr.link!=null){
                ptr=ptr.link;
            }
            ptr.link=temp;
        }
    }
    //Now display
    public static void display(){
        if(head==null){
            System.out.println("LinkedList is Empty");
        }
        else{
            Nodee ptr=head;
            while(ptr!=null){
                System.out.println(ptr.data);
                ptr=ptr.link;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        do{
            System.out.println("Enter the Element ");
            int ele=sc.nextInt();
            insert(ele);
            System.out.println(ele+"  pushed.....");
            System.out.println();
            System.out.println("Do you want to continue press 1");
        }while(sc.nextInt()==1);
        System.out.println("displaying the linked list");
        display();
    }
}
