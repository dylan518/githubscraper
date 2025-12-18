import java.util.*;

public class Main {
    public static void main(String[] args) {

        // PRIMITIVE
        // int x;
        // float z;
        // char a;
        // double b;
        // boolean y;
        // byte i;

        

        //NON PRIMITIVE
        // String name;
        // Student ab;

        //WRAPPER CLASS
        // Integer s;
        // Float d;
        // Character f;
        // Double g;
        // Boolean h;
        // Byte j;

        // ArrayList<String> names = new ArrayList<String>();
        // names.add("Enola Homes");
        // names.add("Elaizabeth McQueen");
        // names.add("Tailor Swiftly");


        
        
        // names.remove(1);
        // System.out.println(names.size());

        //  
        // names.remove(0);
        // System.out.println(names.get(0));

        // System.out.println(names.get(0));
        // names.set(0,"Emma Watson");
        // System.out.println(names.get(0)); 

        // String name =  names.get(1);
        // System.out.println(name);

        ArrayList<Student> students  = new ArrayList<Student>();
        students.add(new Student("Enola Homes", "Bachelor in Criminal Justice"));
        students.add(new Student("Elaizabeth McQueen", "Bachelor of Arts major in Political Science"));
        students.add(new Student("Tailor Swiftly", "Fine Arts"));

        for (int i = 0; i < students.size(); i++) {
            students.get(i).introduce();
        }

        // students.get(1).introduce();

        // students.set(0, new Student("Travis Klay ", " Bachelor of Science in Accountancy"));
        // students.remove(1);
        // students.get(1).introduce();

        }

}
