package FunctionsAssignmentAndPractices;

public class BackToSenderLogisticsService {
    public static int calculateRidersPayment(int successfulDeliveries){
        int commission = 0;
        if (successfulDeliveries < 50){
            commission = successfulDeliveries * 160 + 5000;
        }
        if (successfulDeliveries  >= 50 && successfulDeliveries <= 59){
            commission = successfulDeliveries * 200 + 5000;
        }
        if (successfulDeliveries >= 60 && successfulDeliveries <= 69){
            commission = successfulDeliveries * 250 + 5000;
        }
        if (successfulDeliveries >= 70){
            commission = successfulDeliveries * 500 + 5000;
        }
        return commission;
    }

    public static void main(String[] args) {
        int allowance = calculateRidersPayment(80);
        System.out.println(allowance);
    }
}


