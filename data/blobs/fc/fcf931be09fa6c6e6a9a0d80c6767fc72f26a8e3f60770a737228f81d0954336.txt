public class Atm {

    int iban;
    public Account account;

    public Atm(int iban, String account) {
        this.iban = iban;
        //this.account = account;
    }

    // сеттер назначает account для класса Atm из класса Account
    public void setAccount(Account account) {
        this.account = account;
    }

    // метод, который связывает atm и account
    public void go(){
        System.out.println( "Atm " + this.iban + " поехал под управлением - " + account.getPin_cod());
    }
    public Account getAccount(){
        return account;
    }

    @Override
    public String toString() {
        return "Atm{" +
                "iban=" + iban +
                ", account=" + account +
                '}';
    }
}
