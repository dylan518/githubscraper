package view;


import model.LeaseModel;
import utils.CustomDate;

import java.util.Calendar;
import java.util.Scanner;



public class LeaseView {

    public static LeaseModel getLeaseDetails(String propertyID) {
        Scanner scan = new Scanner(System.in);

//        System.out.println("Enter Property ID : ");
//        String propertyID= scan.next();

        System.out.println("Enter Tenant ID : ");
        String tenantID= scan.next();

        System.out.println("Enter Start Date [DD/MM/YYYY] of Lease : ");
        String sDate= scan.next();
        Calendar startDate = CustomDate.getDate(sDate);

        System.out.println("Enter End Date [DD/MM/YYYY] of Lease : ");
        String eDate= scan.next();
        Calendar endDate = CustomDate.getDate(eDate);

        System.out.println("Enter the Rent Amount : ");
        double amount= scan.nextDouble();

        return new LeaseModel(propertyID,tenantID,startDate,endDate,amount);
    }

    public void printLeaseDetails(String leaseID,LeaseModel lease) {
        System.out.println("Lease ID : "+leaseID);
        System.out.println(lease);
    }
}
