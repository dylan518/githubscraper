public class Accounts {
    private int accno;
    private String accname;
    private double balance;

    public Accounts(int accno, String accname, double balance) {
        this.accno = accno;
        this.accname = accname;
        this.balance = balance;

    }
    public void deposit(double amount) {

        balance += amount;
        System.out.println("Deposited" + amount);

    }
    public void withdraw(double amount) {

        if(balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn" + amount);
        }
        else {
            System.out.println("insufficient balanace");

        }
            ;
        }
        System.out.println("Withdrawn" + amount);
    }
}
