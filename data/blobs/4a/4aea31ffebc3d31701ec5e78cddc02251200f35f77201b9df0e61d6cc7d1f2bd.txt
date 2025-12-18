package queues;
import java.util.*;

public class interleaveQueue {
    //interleave 2 halves of a queue by using just one extra queue: for even length only
    
    public static void Interleave(Queue<Integer> q){
        Queue<Integer> u = new LinkedList<>() ;
        int size = q.size();
        for(int i=0;i<size/2;i++){
            u.add(q.remove());
        }
        while(!u.isEmpty()){
            q.add(u.remove());
            q.add(q.remove());

        }

    }
    public static void printQ(Queue q){
        while(!q.isEmpty()){
        System.out.print(q.remove()+ " ");
        }
    }
    public static void main(String args[]){
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        q.add(2);
        q.add(3);
        q.add(4);
        q.add(5);
        q.add(6);
        q.add(7);
        q.add(8);
        
        Interleave(q);
        System.out.println(" ");
        printQ(q);
        

    }
}
