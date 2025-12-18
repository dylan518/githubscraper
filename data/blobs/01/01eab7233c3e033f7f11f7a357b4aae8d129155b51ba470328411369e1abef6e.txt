package day45_custom_classes;

import day45_custom_classes.Offer;

import java.util.ArrayList;
import java.util.Arrays;

public class UsingOffer {
    public static void main(String[] args) {
        Offer offer1=new Offer("Apple","Boston",200000,false,15);//created first offer object
        ArrayList<Offer>list= new ArrayList<>();
        list.add(offer1);
        list.add(new Offer("Google","NewYork",190000,true,13));//this a way to create and add
        //another object at the same time
        System.out.println();
        Offer[]moreOffers={
               new Offer("Samsung","Philadelphia",190000,true,15),
               new Offer("TDBank","Boston",180000,true,13),
               new Offer("Target","Newport",185000,false,12),

       };
        list.addAll(Arrays.asList(moreOffers));//added the array of Offers into the ArrayList of Offers

        list.addAll(Arrays.asList(
                new Offer("CVS","Denver",100000,true,12),
                new Offer("Walgreens","Chicago",120000,true,10)
        ));//added offer objects using the var args of the asList method to add multiple Offer objects
        System.out.println("__________________________________________");
        System.out.println();
        System.out.println(list);

        //create arrayList to filter the Offers
        ArrayList<Offer>salaries=new ArrayList<>(list);
        salaries.removeIf(each->each.salary<170000);
        System.out.println("Salaries above $170000");
        System.out.println(salaries);
        System.out.println("______________________________________________________");

        ArrayList<Offer>fullTime=new ArrayList<>(list);
        fullTime.removeIf(each->!each.isFullTime);
        System.out.println(fullTime);
        System.out.println("_____________________________________________________");
        ArrayList<Offer>local=new ArrayList<>(list);
        for(int i=0;i<list.size();i++){
            if(list.get(i).location.equals("Boston")||list.get(i).location.equals("Springfield")){
                local.add(list.get(i));
            }
        }

        System.out.println("Local offers: :"+local);
        System.out.println("FullTime offers: "+fullTime);
    }
}
