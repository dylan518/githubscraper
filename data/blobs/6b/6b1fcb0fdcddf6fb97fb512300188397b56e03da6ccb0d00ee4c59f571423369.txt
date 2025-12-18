//Write a Java program to get an element in a tree set which is strictly greater than the given element.
import java.util.*;
class Test14
{
	public static void main(String arg[])
	{
		TreeSet<Integer> set=new TreeSet<Integer>();
		set.add(1);
		set.add(82);
		set.add(35);
		set.add(24);
		set.add(505);
		set.add(60);
		set.add(07);
		set.add(88);
		set.add(19);
		set.add(110);
		System.out.println("set: "+set);
		System.out.println("Strictly lower than 88 : "+set.lower(88));
	}
}