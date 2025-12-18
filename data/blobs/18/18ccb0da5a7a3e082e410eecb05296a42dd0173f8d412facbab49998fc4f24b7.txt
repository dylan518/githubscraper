package inheritance;
class BankAccountDetails
{
	 int Deposite=20000;
	 int Withdraw=5000;
	 
	 int depositeAmount;
	 int withdrawAmount;
	 float intrestRate=9.5f;
	
    public void depositeMoney()
    {
    	System.out.println("Deposite = "+Deposite );
    }
    public void WithdrawMoney()
    {
    	int balance=depositeAmount - withdrawAmount;
    	System.out.println("Withdraw = "+ Withdraw);
    	//System.out.println("Balance = " +balance );
    	
    }
    public void balance()
    {
    	int balance=depositeAmount - withdrawAmount;
    	System.out.println("Balance = " +balance );
    }
}
class NRIAccount extends BankAccountDetails
{
	public void applyFixedDeposite()
	{
		//super.balance();
		super.intrestRate=6.5f;
		System.out.println("intrest for NRIAccount is ="+intrestRate);
	}
}
class SeniorCitizen extends BankAccountDetails
{
	public void applyFixedDeposite()
	{
		//super.depositeMoney();
		//super.Withdraw
		super.intrestRate=10.5f;
		System.out.println("intrest for SeniorCitizen is ="+intrestRate);
	}
}
public class BankAccount
{
	public static void main(String[] args)
	{
		
		NRIAccount obj =new NRIAccount ();
		   
		obj.depositeMoney();
		obj.WithdrawMoney();
		obj.balance();
		obj.applyFixedDeposite();
		   
	  SeniorCitizen obj1=new SeniorCitizen();
	       
		    obj1.applyFixedDeposite();
		    
	}
}


