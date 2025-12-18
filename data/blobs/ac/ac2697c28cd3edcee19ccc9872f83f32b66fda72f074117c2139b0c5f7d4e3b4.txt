/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package salary;

/**
 *
 * @author USER
 */
public class jenis {
    private int id_jenis;
    private String nm_jenis;
    
    public jenis(int id_jenis, String nm_jenis){
        this.id_jenis = id_jenis;
        this.nm_jenis = nm_jenis;
    }
    
    public int getId_Jenis(){
        return id_jenis;   
    }
    public void setId_Jenis (int id_jenis){
        this.id_jenis = id_jenis;
    }
    
    public String getNm_Jenis(){
        return nm_jenis;   
    }
    public void setNm_Jenis (String nm_jenis){
        this.nm_jenis = nm_jenis;
    }
}
