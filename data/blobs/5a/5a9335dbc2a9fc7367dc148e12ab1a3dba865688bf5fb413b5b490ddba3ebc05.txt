/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javaapplication3.models.agentSubClass;

import java.util.HashMap;
import javaapplication3.models.Agent;
import javaapplication3.models.Area;

/* Denna fil hanterar subklassen Kontorschef som kommer ifrån superklassen Agent. I denna subklass klonas redan existerande objekt för att sedan
 * kunna ersättas med ett redigerat objekt av Kontorschef. */

public class KontorsChef extends Agent {
    String kontorsbeteckning;
    
    /* Konstruktorn tar in en HashMap, ett area-objekt och en sträng som parameter för skapa ett objekt, samt pekar på 
     * vart informationen skall lagras.*/
    public KontorsChef(HashMap<String, String> agentMap, Area area, String officeName){
        super(agentMap,area); // Anropar superklassens konstruktor.
        this.kontorsbeteckning = officeName;
    }
    
    // Denna metod skapar ett tomt objekt för redigering.
    public KontorsChef(){
        super();
    }
    
    //Denna metod klonar ett redan existerande objekt för att senare kunna ersätta befintligt. 
    public void cloneObject(KontorsChef other) {
        super.cloneObject(other);
        this.kontorsbeteckning = other.kontorsbeteckning;
    }
    
    // Setter för kontorsbetäckningen
    public void setOfficeName(String name){
        kontorsbeteckning = name;
    }
    
    // Getter för kontorsbetäckningen
    public String getOfficeName(){
        return kontorsbeteckning;
    }
}
