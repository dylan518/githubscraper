/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package election.Persona;

/**
 *
 * @author kal bugrara
 */
public class Person {
    
    String name;
    public Person (String name){
        
        this.name = name;
    }
    public String getPersonByName(){
        return name;
    }

        public boolean isMatch(String n){
        if(getPersonByName().equals(n)) return true;
        return false;
    }
    
}
