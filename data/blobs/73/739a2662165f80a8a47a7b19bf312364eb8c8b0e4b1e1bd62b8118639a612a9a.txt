package _11_Stream_Coding.terminal_operation;

import java.util.ArrayList;
import java.util.List;

public class forEach {

	public static void main(String[] args) {
	  
		/**
		 *     
		 *     **) The forEach() method performs an action for each element in the stream.
		 *     **)  It is typically used for printing or other side effects.
		 */
		
		List<String> courseList = new ArrayList<>();
		courseList.add("Java Guides");
		courseList.add("Python Guides");
		courseList.add("C Guides");
		
		courseList.stream().forEach(System.out::println);

	}

}
