public class FullMultiplicationTable{
   public static void main(String [] args){
	for(int number = 1; number < 10; number++){
		for(int times = 1; times < 10; times++){
			int product = number * times;
			System.out.printf("%d * %d = %d\t",times,number,product);
			}
			System.out.println();
		}
	}
}