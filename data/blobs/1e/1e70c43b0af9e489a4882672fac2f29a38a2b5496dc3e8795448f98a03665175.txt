import java.util.ArrayList;
import java.util.Iterator;

public class EmployeesTester {
    public static void main(String[] args) {
        Employees emps = new Employees();


        ArrayList<Integer> l  = new ArrayList<>();

        for(Integer e : emps){
            System.out.println(e);
        }


        Iterator i =emps.iterator();
        while (i.hasNext()){
            System.out.println(i.next());
        }

    }
}

