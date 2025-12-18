//import static org.junit.Assert.assertTrue;
//import static org.junit.jupiter.api.Assertions.assertTrue;
//import static org.testng.Assert.assertEquals;
//import static org.testng.Assert.assertTrue;
//
//import org.junit.Test;
package coding;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import org.junit.Test;
public class AssignmentOperatorTest {

	//@Test
	//public void AssignmentOperator() {
		/* int num = 10;
		num +=2;
		assertEquals(12, num);
		System.out.println(num);
		num -=2;
		assertEquals(10, num);
		System.out.println(num);
		num *=2;
		assertEquals(20, num);
		System.out.println(num);
		num %=2;
		assertEquals(0, num);
		System.out.println(num);	*/
		 
//		public static String CatCount(int numberOfCats) {
//		return numberOfCats == 1 ? "cat" : "cats";
	
//	public void CatCount() {
//		assertEquals("cat", catOrCats());
//				
//		
//	}
//
//	private String catOrCats() {
//		String cat = "cat";
//		return cat ;
//		
//	
//	}
//	@Test
//	public void IfValidation() {
//		int a =5;
//				if(a>10);
//				//System.out.println(a);
//				assertEquals(a, 5);
//		return;
		
//	@Test
//	public void TruthValidation() {
//		boolean truthy = true;
//		if(truthy) {
//			assertTrue(truthy);
//		}
	@Test
		public void TruthAndFalse() {
			boolean truthy = false;
			if(truthy)
				assertTrue(truthy);
			assertFalse(!truthy);
			
		}
	}

	
