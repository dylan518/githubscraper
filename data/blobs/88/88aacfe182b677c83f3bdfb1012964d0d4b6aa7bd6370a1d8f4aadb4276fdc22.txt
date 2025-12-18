package com.demo.ExceptionHandling;

class Amount {
    private String currency;
    private int amount;

    public Amount(String currency, int amount) {
        super();
        this.currency = currency;
        this.amount = amount;
    }

    //when throwing a checked exception your method needs to have "throws Exception" in the signature"
    // when throwing a unchecked exception your method does not need "throws ..." in signature.
    public void add(Amount other) {
        //if currency do not match throw new Exception "Currency Don't match"
        if(!this.currency.equals(other.currency)) {
            //throw new Exception("Currency Don't Match " + this.currency + " & " + other.currency);
            throw new CurrenciesDoNotMatchException("Currency Don't Match " + this.currency + " & " + other.currency);

        }
        this.amount = this.amount + other.amount;
    }

    public String toString() {
        return amount + " " + currency;
    }

    // to create an unchecked exception add "extends RuntimeException
class CurrenciesDoNotMatchException extends RuntimeException {
    public CurrenciesDoNotMatchException(String msg) {
        super(msg);
    }
}
}
public class ThrowingException {
    public static void main(String[] args) throws Exception {
        Amount amount1 = new Amount("USD", 10);
        Amount amount2 = new Amount("EUR", 20);
        amount1.add(amount2);
        System.out.println(amount1);
    }
}
