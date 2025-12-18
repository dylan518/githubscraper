/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package model;

import data.DBUtil;
import java.io.Serializable;
import java.text.NumberFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.EntityManager;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.OneToOne;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import model.User;
/**
 *
 * @author ADMIN
 */
@Entity
@Table(name = "invoice")
public class Invoice implements Serializable 
{
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long invoiceID;
    
    @ManyToOne( fetch=FetchType.LAZY)
    @JoinColumn(name="userID")
    private User user;
    
    @OneToMany(cascade = CascadeType.ALL, fetch=FetchType.LAZY)
    private ArrayList<LineItem> items; 
    
    private String date;
    private String paymentMethods;
    private String price;

    public Invoice() 
    {
        items = new ArrayList<LineItem>();
    }

    public Long getInvoiceID() {
        return invoiceID;
    }

    public void setInvoiceID(Long invoiceID) {
        this.invoiceID = invoiceID;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public ArrayList<LineItem> getItems() {
        return items;
    }

    public void setItems(ArrayList<LineItem> items) {
        this.items = items;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getPaymentMethods() {
        return paymentMethods;
    }

    public void setPaymentMethods(String paymentMethods) {
        this.paymentMethods = paymentMethods;
    }
    
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    
    public double getInvoiceTotal() {
        double total = 0;
        for (LineItem item : items) {
            total += item.getTotal();
        }
        return total;
    }

    public String getInvoiceTotalCurrencyFormat() {
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        return currency.format(this.getInvoiceTotal());
    }
    
    public static Invoice createInvoice(Cart cart, User user, String paymentMethod) {
        Invoice invoice = new Invoice();
        //User existingUser = getUserFromDatabase(user.getEmail());
        //invoice.setUser(existingUser);
        invoice.setUser(user); // Set the user for the invoice
        invoice.setDate(getCurrentDate()); // Set the current date or use a date format that suits your application
        invoice.setPaymentMethods(paymentMethod); // Set the payment method
        
        // Copy the items from the cart to the invoice
        ArrayList<LineItem> cartItems = cart.getItems();
        if (cartItems != null && !cartItems.isEmpty()) {
            ArrayList<LineItem> invoiceItems = new ArrayList<>();
            double total = 0;

            for (LineItem cartItem : cartItems) {
                LineItem invoiceItem = new LineItem(cartItem.getTour(), cartItem.getQuantity());
                invoiceItems.add(invoiceItem);
                total += invoiceItem.getTotal();
            }
            NumberFormat currency = NumberFormat.getCurrencyInstance();
            invoice.setPrice(currency.format(total));
            invoice.setItems(invoiceItems);
        }

        return invoice;
    }
    
//    public static Invoice createInvoice(Cart cart, User user, String paymentMethod) {
//    Invoice invoice = new Invoice();
//
//    // Retrieve the existing user from the database
//    User existingUser = getUserFromDatabase(user.getEmail());
//    
//    // If the user doesn't exist, persist the new user to the database
//    if (existingUser == null) {
//        // Persist the new user to the database
//        EntityManager entityManager = DBUtil.getEmFactory().createEntityManager();// Obtain your entity manager (you need to implement this part)
//        entityManager.getTransaction().begin();
//        entityManager.persist(user);
//        entityManager.getTransaction().commit();
//        
//        // Now, retrieve the user from the database again
//        existingUser = getUserFromDatabase(user.getEmail());
//    }
//
//    // Set the existing user for the invoice
//    invoice.setUser(existingUser);
//    invoice.setDate(getCurrentDate());
//    invoice.setPaymentMethods(paymentMethod);
//
//    // Copy the items from the cart to the invoice
//    ArrayList<LineItem> cartItems = cart.getItems();
//    if (cartItems != null && !cartItems.isEmpty()) {
//        ArrayList<LineItem> invoiceItems = new ArrayList<>();
//        double total = 0;
//
//        for (LineItem cartItem : cartItems) {
//            LineItem invoiceItem = new LineItem(cartItem.getTour(), cartItem.getQuantity());
//            invoiceItems.add(invoiceItem);
//            total += invoiceItem.getTotal();
//        }
//
//        NumberFormat currency = NumberFormat.getCurrencyInstance();
//        invoice.setPrice(currency.format(total));
//        invoice.setItems(invoiceItems);
//    }
//
//    return invoice;
//}


    private static String getCurrentDate() 
    {
        //Lấy ngày hiện tại
        LocalDate currentDate = LocalDate.now();

        // Định dạng ngày thành chuỗi
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("YYYY-MM-dd");
        return currentDate.format(formatter);
        
    }
}
