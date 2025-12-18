package homeWorkClass30;
import java.util.Map;
import java.util.TreeMap;

/*Create a Person class with following private fields: name, lastName, age, salary.
       Variables should be initialized through constructor.
       Inside the class also create a method to print user details.
       In Test Class create a Map that will store key in ascending order.
       In that map store personId and a Person Object. Print each object details*/
public class Person {
 String name;
 String lastName;
 int age;
 double salary;
  public Person(String name, String lastName, int age, double salary) {
   this.name = name;
   this.lastName = lastName;
   this.age = age;
   this.salary = salary;}
   void printUserDetails(){
    System.out.println(name+" "+lastName+" "+age+" "+salary);
  }
 }
 class Tester{
  public static void main(String[] args) {
   Map<Integer,Person>map=new TreeMap<>();
   map.put(23546,new Person("John","Snow",29,95000));
   System.out.println(map);
  }
 }
