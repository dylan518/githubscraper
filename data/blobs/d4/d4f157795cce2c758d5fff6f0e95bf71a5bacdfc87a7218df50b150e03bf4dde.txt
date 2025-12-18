/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package minggu2p1_tugasno1;

import java.util.Scanner;
public class WS_SI_M2P2Coba_no2 {

    public static void main(String[] args) {
       String lampu;
       Scanner scan = new Scanner(System.in);
       
       //mengambil input 
        System.out.println("input nama warna:");
        lampu = scan.nextLine();
        
        switch(lampu){
            case "merah":
                System.out.println("Lampu merah, Berhenti!");
                break;
            case "kuning":
                System.out.println("Lampu kuning, Hati-Hati!");
                break;
            case "hijau":
                System.out.println("Lampu hijau, Silahkan Jalan!");
                break;
            default:
                System.out.println("Warna lampu salah!");
        }
    }
    
}
