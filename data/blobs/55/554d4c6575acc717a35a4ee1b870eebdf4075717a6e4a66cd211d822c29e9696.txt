package dsa;


class Node{
	int data;
	Node next;
	
	public Node(int data) {
		this.data=data;
		this.next=null;
	
	}
	
	public void printNode(Node head) {
		Node curr = head;
		while(curr!=null) {
			
			System.out.print(curr.data+" ");
			
			
//			if(curr.next==null) {
//				System.out.println("last node :"+curr.data);
//		}
			curr= curr.next;
		
			
		
	}
		
		
	}
	
	public void Reverse(Node head) {
		Node curr = head;
		
		Node previous= null;
		while(curr!=null ) {
			Node temp = curr.next;
			
			curr.next = previous;
			//System.out.println(curr.next.data);
			
			previous= curr;
			
			
			curr= temp;
			
		}
		
		
		head= previous;
		
	    head.printNode(head);
		
	}
	
	 public Node MiddleList(Node head) {
	        Node slow = head;
	        Node fast = head;
	        while (fast != null && fast.next != null) {
	            fast = fast.next.next;
	            slow = slow.next;
	        }
	        System.out.println("middle element:"+slow.data);
	        return slow;
	    }
	 
	public void deleteMiddle(Node head) {

	        Node slow = head;
	        Node fast = head;
	        Node pre = null;
	        
	        while(fast!=null && fast.next!=null){
	         fast = fast.next.next;
	            pre = slow;
	            slow = slow.next;
	           
	        }
	          pre.next= slow.next;
	        System.out.println("delihjxs");
	        head.printNode(head);
	        
	    }
	
	 
	 public void DeleteLastNode(Node head) {
		 Node curr= head;
		 Node previous = null;
		
			  while (curr.next != null) {
		            previous = curr;
		            curr = curr.next;
		            System.out.println(previous.data);
		            System.out.println();
		            System.out.println(curr.data);
		        }

		        // Delete the last node
			  System.out.println("current next:"+curr.next);
		        previous.next = curr.next;
		        System.out.println("after deleting:");
		        head.printNode(head);
		    }
	 
	 
	 
	 public Node DeleteMiddleNode(Node head) {
		 
		
	
		Node pre = null;
		Node slow =head;
		Node fast = head;
		
		while(fast!= null && fast.next!=null){
			
			pre = slow;
			slow = slow.next;
			fast = fast.next.next;
			
		}
		pre.next = slow.next;
		return pre;
		 
	 }
	        
		}
		 
	 

public class LinkedListt {
	
	public static void main(String[] args) {
		
		Node head = new Node(1);
		head.next = new Node(2); //create new Node and link it with head
		head.next.next= new Node(3);
		head.next.next.next = new Node(4);
		head.next.next.next.next= new Node(7);
		//System.out.println(head.next.data);
		//  head.printNode(head);
		head.printNode(head);
		
		head.DeleteMiddleNode(head);
		head.printNode(head);
		head.DeleteLastNode(head);
		  head.Reverse(head);
		  head.deleteMiddle(head);
		
		
	}

}


