package collection_;

import java.util.HashSet;
import java.util.Objects;

/**
 * @author hucc
 * 2022/3/25 23:15
 */
@SuppressWarnings("all")
public class HashSetExercise2 {


    public static void main(String[] args) {

        HashSet hashSet = new HashSet();
        hashSet.add(new Employee2("Tom", 15000, new MyDate(2022, 3, 25)));
        hashSet.add(new Employee2("Tom", 15000, new MyDate(2022, 3, 25)));
        hashSet.add(new Employee2("Tom", 15000, new MyDate(2022, 3, 25)));
        System.out.println(hashSet);

    }

}

@SuppressWarnings("all")
class Employee2 {

    private String name;
    private int sal;
    private MyDate birthday;

    public Employee2(String name, int sal, MyDate birthday) {
        this.name = name;
        this.sal = sal;
        this.birthday = birthday;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Employee2 employee2 = (Employee2) o;
        return sal == employee2.sal && name.equals(employee2.name) && birthday.equals(employee2.birthday);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, sal, birthday);
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", sal=" + sal +
                ", birthday=" + birthday +
                '}';
    }
}

@SuppressWarnings("all")
class MyDate {

    private int year;
    private int month;
    private int day;

    public MyDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        MyDate myDate = (MyDate) o;
        return year == myDate.year && month == myDate.month && day == myDate.day;
    }

    @Override
    public int hashCode() {
        return Objects.hash(year, month, day);
    }

    @Override
    public String toString() {
        return year + "-" + month + "-" + day;
    }
}
