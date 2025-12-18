import java.util.Collection;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;

public class LinkedListDemo {
    public static void main(String[] args) {
        // Declare Linked List

        // LinkedList <Integer> LL = new LinkedList<Integer>();
        // LinkedList <String> LL = new LinkedList<String>();
        LinkedList l = new LinkedList();

        // add element in the linked list
        l.add(100);
        l.add("welcome");
        l.add(15.5);
        l.add('A');
        l.add(true);
        l.add(null);

        System.out.println(l);

        System.out.println(l.size());

        // removing
        l.remove(3);
        // l.remove('A');
        System.out.println(l);

        // inserting/deleting in the middle of ll
        l.add(3, "java");

        // retreiving the value
        System.out.println(l.get(3));

        // change the value
        l.set(5, "X");

        // contains()
        System.out.println(l.contains("java"));

        // empty()
        System.out.println(l.isEmpty());

        // reading data 

        // reading data from using for loop
        for(int i=0;i<l.size();i++){
            System.out.println(l.get(i));
        }
        
        // by using for..each loop
        for(Object value:l){
            System.out.println(value);
        }

        // by using iterator method
        Iterator it = l.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }

        // adding/removing multiple elements into the ll
        LinkedList ll = new LinkedList();
        ll.add("X");
        ll.add("Y");
        ll.add("Z");
        ll.add("A");
        ll.add("B");
        ll.add("C");

        ll.addAll(l);

        ll.removeAll(l);
        System.out.println(ll);

        // sorting and shuffling

        Collections.sort(ll);
        System.out.println(ll);

        Collections.shuffle(ll);
        System.out.println(ll);

        // reverse order
        Collections.sort(ll,Collections.reverseOrder());
        System.out.println(ll);


        // Implementing stacks and queue concepts

        LinkedList animal = new LinkedList<>();
        animal.add("Dog");
        animal.add("cat");
        animal.add("horse");
        animal.add("Dog");

        animal.addFirst("Tiger");
        animal.addLast("Elephant");
        System.out.println(animal);

        System.out.println(animal.getFirst());
        System.out.println(animal.getLast());

        animal.removeFirst();
        animal.removeLast();
        System.out.println(animal);
    }
    
}
/*
 * LinkedList is a class which is implemented from List interface as well as Dequeue Interface
 * Duplicates element allowed 
 * null value are also allowed
 * insertion order preserved
 * indexing is also present
 * in linked list elements are stored at random locations
 * always retrieval starts from first node
 * In collections the linkedlist is Doubly Linked List
 * linked list is also used in generating stacks and queues
 * 
 * Retrieving is best in ArrayList
 * Insertion/Deletion is best in LinkedList (due to shifting)
 * 
 * 
 * ll.add(Object e)
 * ll.add(index,data)
 * ll.addAll(Collection C)
 * ll.remove(Object e)
 * ll.remove(index)
 * ll.removeAll(Collection C)
 * ll.get(index)
 * ll.set(index, Object e)
 * Colections.sort(ll)
 * Colections.shuffle(ll)
 * 
 * addFirst(object)  // add element at the first position
 * addLast(object)  // add element at the last position
 * removeFirst(Object)// remove element of the first position
 * removeLast(Object)// remove element of the last position
 * getFirst() //gives the first elment/node from the LL
 * getLast()  //gives the last elment/node from the LL
 */