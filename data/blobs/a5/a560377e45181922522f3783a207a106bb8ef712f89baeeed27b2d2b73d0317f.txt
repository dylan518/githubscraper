
package Oopspkg;

import java.util.Scanner;

interface bank
{
 void accoundetails();
 void balance();
 void withdraw();
 void deposit();
}

class SBI implements bank
{
	Scanner sc=new Scanner(System.in);
	int bal=5000,wdraw,amt,no,deposit;
	String name="";
	@Override
	public void accoundetails() {
		System.out.println("Enter the customer name");
		name=sc.nextLine();
		System.out.println("Enter the accountno: ");
		no=sc.nextInt();
		
	}

	@Override
	public void balance() {
		System.out.println("Account no="+no);
		System.out.println("Available balance="+bal);
		
	}

	@Override
	public void withdraw() {
		System.out.println("Your current balance= "+bal);
		System.out.println("Enter the amount to withdraw:");
		amt=sc.nextInt();
		wdraw=bal-amt;
		System.out.println("The remaining balance: "+wdraw);
		bal=wdraw;
		
	}

	@Override
	public void deposit() {
		System.out.println("Enter the amount to depost: ");
		deposit=sc.nextInt();
		bal=bal+deposit;
		System.out.println("your final balance=" +bal);	}
}
		

public class Interfacebankproblem {

	public static void main(String[] args) {
		SBI ob=new SBI();
		ob.accoundetails();
		ob.balance();
		ob.withdraw();
		ob.deposit();
		

	}

}





