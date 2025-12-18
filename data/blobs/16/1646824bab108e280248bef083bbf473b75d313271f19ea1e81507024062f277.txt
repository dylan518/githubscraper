import java.util.ArrayList;
import java.util.Collections;

/*
 * Comparable program for sorting object by any one proprerty from the object using Comparable interface 
 */

class Person implements Comparable<Person> {
    String name;
    int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public int compareTo(Person person) {
        return this.age - person.age;
    }

    @Override
    public String toString() {
        return "Person [name=" + name + ", age=" + age + "]";
    }
}

public class ComparableProgram {

    public static void main(String args[]) {
        ArrayList<Person> personList = new ArrayList<>();
        personList.add(new Person("Ravi", 24));
        personList.add(new Person("Dipak", 23));
        personList.add(new Person("Juned", 23));

        System.out.println("Person List : " + personList);
        Collections.sort(personList);
        for (Person person : personList) {
            System.out.println(person.name + " " + person.age);
        }
    }

}
