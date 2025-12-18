package OOP;

public class Account {

    private String number;
    private double balance;
    private String customerName;
    private String customerEmail;
    private String customerPhone;

    //constructor Test

    public Account() {
        // constructor chaining
        // call to 'this()' must be first statement in constructor body
        this("123456789", 100, "DefaultName", "default@gmail.com", "111111");

        System.out.println("Empty constructor called.");
    }

    public Account(String number, double balance, String customerName, String customerEmail, String customerPhone) {

        this.number = number;
        this.balance = balance;
        this.customerName = customerName;
        this.customerEmail = customerEmail;
        this.customerPhone = customerPhone;

        System.out.println("constructor with parameters.");
    }

    public Account(String customerName, String customerEmail, String customerPhone) {
        this("99999", 100, customerName, customerEmail, customerPhone);
//        this.customerName = customerName;
//        this.customerEmail = customerEmail;
//        this.customerPhone = customerPhone;
    }

    public void depositFunds(double depositAmount) {
        balance = balance + depositAmount;
        System.out.println("Deposit amount is " + depositAmount);
        System.out.println("New balance is " + balance);
    }

    public void withdrawFunds(double withdrawalAmount) {
        if (balance - withdrawalAmount < 0) {
            System.out.println("Insufficient funds.");
            System.out.println("current balance is " + balance);
        } else {
            balance = balance - withdrawalAmount;
            System.out.println("Withdrawn balance is " + withdrawalAmount);
            System.out.println("current balance is " + balance);
        }
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getCustomerEmail() {
        return customerEmail;
    }

    public void setCustomerEmail(String customerEmail) {
        this.customerEmail = customerEmail;
    }

    public String getCustomerPhone() {
        return customerPhone;
    }

    public void setCustomerPhone(String customerPhone) {
        this.customerPhone = customerPhone;
    }
}
