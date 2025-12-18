import java.util.*;

class SeatFilled extends Exception {
    String Error;

    SeatFilled() {
        Error = "Seat Filled Already";
    }
}

class Student {
    int reg;
    String Name;
    short SEM;
    float cgpa;
    GregorianCalendar g1;
    static int count = 0;
    SeatFilled s1;

    Student() {
        count++;
    }

    Student(String a, int b, int c, int d, short e, float f) throws SeatFilled {
        s1 = new SeatFilled();
        if (count >= 25) {
            throw s1;
        }
        g1 = new GregorianCalendar(d, c, b);
        int s = d % 100;
        int t = s * 100 + count;
        reg = t;
        Name = a;
        SEM = e;
        cgpa = f;
        count++;
    }

    void Display() {
        System.out.print("\n Name of Student : " + Name + "\n Registration Number of Student : " + reg
                + "\n Semester : " + SEM + "\n CGPA : " + cgpa);
    }
}

public class Records {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Number of Students : ");
        int n = sc.nextInt();
        Student[] s1 = new Student[n];
        for (int i = 0; i < n; i++) {
            System.out.println("Details for Student " + (i + 1));
            System.out.print("Name : ");
            String a = sc.next();
            System.out.print("Date of Joining : ");
            int b = sc.nextInt();
            int c = sc.nextInt();
            int d = sc.nextInt();
            System.out.print("Semester : ");
            short e = sc.nextShort();
            System.out.print("CGPA : ");
            float f = sc.nextFloat();
            try {
                s1[i] = new Student(a, b, c, d, e, f);
            } catch (SeatFilled s) {
                System.out.println("Exception Handled " + s.Error);
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.println("Details for Student " + (i + 1));
            s1[i].Display();
        }
        sc.close();
    }
}