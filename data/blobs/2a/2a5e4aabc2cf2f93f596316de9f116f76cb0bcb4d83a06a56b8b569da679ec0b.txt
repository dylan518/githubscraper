package revision;
import java.util.Random;

public class IfElseRandomClass {

	public static void main(String[] args) {
		int rate;
		
		Random rand = new Random();		//CREATES AN ONJECT OF RANDOM CLASS
		
		//THE CODE BELOW GENERATES RANDOM NUMBERS FROM 1 TO 50
		rate = (1+ (Math.abs(rand.nextInt()))%50);					//Assign random numbers to rate
																	//abs() method of Math class is used to get absolute value of random numbers
		System.out.println("Rate = "+rate);
		
		if(rate>=40)
			System.out.println("You can buy what you need");
		else
			if(rate>=30)
				System.out.println("You can buy 1.5 times what you need");
			else
				if(rate==20)
					System.out.println("You can buy 2 times what you need");
				else
					if(rate<20)
						System.out.println("You can buy 2.5 times the quantity you need");
		
	}

}
