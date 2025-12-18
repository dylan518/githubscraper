/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package minggu1;

/**
 *
 * @author knoyan
 */
public class Laptop extends Devices {
    private int battery;
    private String watt;
    
    public Laptop(String m, int r, String p, String g, String s, int v, String ps, int b) {
        super(m, r, p, g, s, v);
        watt = ps;
        battery= b;
    }
    
    public void infolaptop(){
        super.info();
        System.out.println("Watt: " + watt);
        System.out.println("Battery: " + battery + "%");
    }


    
}
