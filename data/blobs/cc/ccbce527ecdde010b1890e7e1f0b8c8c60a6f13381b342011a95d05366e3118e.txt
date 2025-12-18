
import java.time.LocalDate;  
import java.util.ArrayList;
/**
 *
 * @author Doaa Said
 */
public  class Order {
 private String ID;
 private Customer customer;
private LocalDate shipping_date;
private ArrayList<Products>productslist=new ArrayList<Products>();
private double totalCostbeforeoffer=0;
private double totalCostafteroffer;
String payment;
private boolean isShipped;


    public Order(String ID,Customer customer, ArrayList<Products>productslist) {
        this.ID=ID;
        this.customer = customer;
       
        this.productslist=productslist;
        
calculate_costbeforeoffer(); 
    calculate_costafteroffer();
    }

    public String getID() {
        return ID;
    }

    public Customer getCustomer() {
        return customer;
    }

    public LocalDate getShipping_date() {
         LocalDate currentDate = LocalDate.now();
          shipping_date = currentDate.plusWeeks(1);
        return shipping_date;
    }


    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

    public void setPayment(String payment) {
        this.payment = payment;
    }

  private void calculate_costbeforeoffer(){
      for(int i=0;i<productslist.size();i++){
         totalCostbeforeoffer+=productslist.get(i).getPriceAfterDiscount();
      
      }
}
 private void calculate_costafteroffer(){
     
   ArrayList<Double>offerpercentages=Admin.getPercentages();
     
   int index=(int) ((totalCostbeforeoffer-Admin.getBase())/(Admin.getStep()));
   
     totalCostafteroffer=totalCostbeforeoffer-(offerpercentages.get(index)*totalCostbeforeoffer);
      }     

    public double getTotalCostbeforeoffer() {
        return totalCostbeforeoffer;
    }

    public double getTotalCostafteroffer() {
        return totalCostafteroffer;
    }
  
  
  
  
  
    public ArrayList<Products> getProductslist() {
        return productslist;
    }

    public String getPayment() {
        return payment;
    }

    public boolean isIsShipped() {
        LocalDate now = LocalDate.now();
          if(now.compareTo(getShipping_date()) < 0) return false;
        //if getOfferPercentage returns 0, there is no offer on this product
        else return true;
        
       
    }

    @Override
    public String toString() {
        return this.customer.username + "ID=" + ID +"\n"+ "shipping_date=" + shipping_date +"\n"+ " productslist=" + productslist +"\n"+ " totalCostbeforeoffer=" + totalCostbeforeoffer +"\n"+ "totalCostbeforeoffer=" + totalCostafteroffer +"\n"+" payment=" +"\n"+ payment +"\n";
    }

   
}
