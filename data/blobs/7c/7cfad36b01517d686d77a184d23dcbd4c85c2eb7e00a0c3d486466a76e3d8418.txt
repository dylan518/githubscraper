/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Armes;

/**
 *
 * @author bapti
 */
public class Epée extends Arme {
    private double finesse;

    public Epée(String nom, double finesse, int niveauAttaque) {
        super(nom, niveauAttaque);
        if (finesse <0 ) finesse = 0;
        else if (finesse >= 100) finesse = 100;
        this.finesse = finesse;
        this.setAttribut(finesse);  
    }

    public double getFinesse() {
        return finesse;
    }

    public void setFinesse(double finesse) {
        if (finesse < 0) finesse = 0;
        else if (finesse > 100) finesse = 100;
        this.finesse = finesse;
    }

    
}
