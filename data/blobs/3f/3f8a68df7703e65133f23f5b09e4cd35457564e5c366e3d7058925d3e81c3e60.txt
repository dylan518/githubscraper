package assignment2;

import java.util.Scanner;

public class Employee {
	int bp,deduction,bonus;
	public void payslip()
	{
		Scanner obj = new Scanner(System.in);
		System.out.println("Enter Basic Pay, Deduction and Bonus: ");
		bp= obj.nextInt();
		deduction = obj.nextInt();
		bonus = obj.nextInt();
	}
}
