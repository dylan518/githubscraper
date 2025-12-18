package JavaFundamentals;

public class StockTransactionProgram {
    public static void main (String [] args){
        int shares = 1000;

        double pricePerShare = 32.87;

        double commission = 0.02;

        double newPricePerShare = 33.92;

        double initialCost = shares * pricePerShare;

        double initialComission = initialCost * commission;

        double resaleAmount = shares * newPricePerShare;

        double resaleCommission = resaleAmount * commission;

        double profit = resaleAmount - (initialCost + initialComission + resaleCommission);

        System.out.print("Joe has $" + String.format("%.2f",initialCost) + " worth of shares. He then paid his broker $"
                + String.format("%.2f",initialComission) + ". After he sold his stocks for $" + String.format("%.2f",resaleAmount)
                + " and paid the broker $" + String.format("%.2f",resaleCommission) + ". The amounf of profit joe made was $"
                + String.format("%.2f",profit));
    }
}