package cooncurrentcollection;

import java.util.Iterator;
import java.util.concurrent.CopyOnWriteArrayList;

public class CopyOnWriteArrayListModificationTest {
    public static void main(String[] args) {
        CopyOnWriteArrayList c=new CopyOnWriteArrayList();
        c.add("A");
        c.add("B");
        c.add("C");

        Iterator itr=c.iterator();
        c.add("D");//this object won't be available at the time of iteration
        while (itr.hasNext()){
            String s=(String) itr.next();
            System.out.println(s);
        }
        System.out.println(c);
    }
}
