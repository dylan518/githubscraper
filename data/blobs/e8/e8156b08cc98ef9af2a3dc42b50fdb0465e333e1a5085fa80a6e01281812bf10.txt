package randomTask;

public class BankAccTest {

    public static void main(String[] args) {

        BankAccount bankaccount = new BankAccount();
        bankaccount.accountNumber= 12345;
        bankaccount.money = 1000;
        bankaccount.deposit();

        System.out.println(bankaccount.accountNumber);
        System.out.println(bankaccount.money);


        System.out.println("___Creating an object of Checking account___");

        Checking checking = new Checking();

        checking.accountNumber = 11111;
        checking.interest = 2.5;

        checking.deposit();//from parent
        checking.transfer();// from child

        System.out.println("___Creating an object of Saving account___");
        Saving save = new Saving();
        save.accountNumber = 3425346;
        save.money = 456457;
        save.profit = 7656;
        save.deposit();
       // save.profit
       // save.interest= 0; sibling features are not available.

        SuperSavings supersaving = new SuperSavings();
        supersaving.superSaving();
        supersaving.profit = 3453645;
       // supersaving.interest= 23545;// sibling features are not available in this class.
        supersaving.accountNumber= 2354653456L;



//finish creating super savings object and see which feature available to that class
                /*  HW:         //finish creating SuperSavings object and see which feature available to that class
@here  HW: Write program for multilevel inheritance where class C inherits from class B and Class B inherits from Class A.

Write program to inherit class A that has method printF which is static and call or reuse that method into class B

Write a Java program called Teacher.  Identify features and 4 behaviour of that Class. Create 3 subclasses MathTeacher,
ChemistryTeacher and PianoTeacher that would have it their own features and behaviour. Test all 4 classes

Slides for tomorrow's class are published on Canvas @everyone
                 */

    }
}
