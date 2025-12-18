package p1;
import java.util.*;
class ATM {
    BankAccount account;
    public ATM(BankAccount account) {
        this.account=account;
    }
    public void start() {
        Scanner sc=new Scanner(System.in);
        int choice;
        do{
            System.out.println("\n===== ATM Menu =====");
            System.out.println("1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. Exit");
            System.out.print("Choose(1/2/3/4): ");
            choice = sc.nextInt();
            switch (choice){
                case 1:
                    System.out.print("Enter amount to deposit: $");
                    double depositAmount = sc.nextDouble();
                    account.deposit(depositAmount);
                    break;
                case 2:
                    System.out.print("Enter amount to withdraw: $");
                    double withdrawAmount = sc.nextDouble();
                    account.withdraw(withdrawAmount);
                    break;
                case 3:
                	System.out.println("Your current balance is: $" + account.getBalance());
                	break;
                case 4:
                    System.out.println("Thank you! Have a nice day!!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }while (choice != 4);
    }
}
class BankAccount{
    double balance;
    public BankAccount(double initialBalance){
        if (initialBalance>=0){
            this.balance=initialBalance;
        } 
        else{
            this.balance=0;
            System.out.println("Initial balance cannot be negative. Setting balance to 0.");
        }
    }
    public void deposit(double amount){
        if(amount>0){
            balance+=amount;
            System.out.println("Successfully deposited: $"+amount);
        } 
        else{
            System.out.println("Deposit amount must be positive.");
        }
    }
    public boolean withdraw(double amount) {
        if(amount>0 && amount<=balance){
            balance-=amount;
            System.out.println("Successfully withdrawn: $" + amount);
            return true;
        } 
        else if(amount>balance){
            System.out.println("Insufficient balance for this withdrawal.");
            return false;
        } 
        else{
            System.out.println("Withdrawal amount must be positive.");
            return false;
        }
    }
    public double getBalance() {
        return balance;
    }
}
public class AtmInterface {
	public static void main(String[] args) {
		double initial_balance=1000.0;
		BankAccount userAccount = new BankAccount(initial_balance);
	    ATM atm = new ATM(userAccount);
	    atm.start();
	}

}
