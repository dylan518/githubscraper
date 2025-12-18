/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Services;

import Entities.User;
import java.util.Scanner;

/**
 *
 * @author drome
 */
public class UserService {
    Scanner read = new Scanner(System.in, "ISO-8859-1").useDelimiter("\n");
    
    public UserService() {
    }
    
    public User createUser(){
        String name;
        Integer age;
        double money;
        System.out.println("-------LET'S CREATE USER-------");
        System.out.print("Digit User Name: ");
        name = read.next();
        System.out.print("Digit User Money");
        money = read.nextDouble();
        System.out.println("Digit USer Age");
        age = read.nextInt();
        return new User(name, age, money);
    }
    
    public User createUser(String name, Integer age, double money){
        
        return new User(name, age, money);
    }
    
    
    
}
