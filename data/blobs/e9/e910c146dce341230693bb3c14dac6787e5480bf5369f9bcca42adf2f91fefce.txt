import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Stream2 {

	public static void main(String[] args) {
		//Case1: you have given array of Strings, you have to sort the array list in such a way that strings having larger length 
		//will come first than strings with smaller length, and if two strings having same length then sort strings according to default
		//natural sorting order.
		
		List<String> names = Arrays.asList("Bhumika","Natasha","Neeraj","Shivani","Nitish","Garima","Deepanshi","Akanksha");
		System.out.println(names.stream().sorted((a,b)->{
			int l1=a.length();
			int l2=b.length();
			if(l1<l2)
				return 1;
			else if(l1>l2)
				return -1;
			else return a.compareTo(b);
		}).collect(Collectors.toList()));
	}
}
