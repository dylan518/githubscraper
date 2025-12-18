/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Security;

import java.nio.charset.StandardCharsets;

/**
 *
 * @author david
 */
public class cripto {
    public String cripto(String message){
        byte[] arr = message.getBytes(StandardCharsets.ISO_8859_1);
        byte[] arr1 = new byte[arr.length];
        byte des = 32;
        for(int i =0;i<arr.length;i++){
            if((arr[i] + des)>127){
                int aux = (arr[i] + des)-127;
                arr1[i] = (byte)(33 + aux);
                }
            else
                arr1[i]= (byte)(arr[i] + des); 
        }
        String s = new String(arr1, StandardCharsets.ISO_8859_1);
        return s;
    }
}
