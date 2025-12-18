/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package quanlyhoadon;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;

/**
 *
 * @author XUAN DINH
 */
public abstract class BENHNHAN implements IVIENPHI{
    protected  String MaBenhNhan, HoTen;
    protected  Date NgayNhap;
    protected  boolean PhongTheoYeuCau;
    protected  Scanner sc;
    protected String LoaiBaoHiem;    
    public abstract String toString();
    public String getMaBenhNhan() {
        return MaBenhNhan;
    }

    public void setMaBenhNhan(String MaBenhNhan) {
        this.MaBenhNhan = MaBenhNhan;
    }

    public String getHoTen() {
        return HoTen;
    }

    public void setHoTen(String HoTen) {
        this.HoTen = HoTen;
    }

    public Date getNgayNhap() {
        return NgayNhap;
    }

    public void setNgayNhap(Date NgayNhap) {
        this.NgayNhap = NgayNhap;
    }

    public boolean getPhongTheoYeuCau() {
        return PhongTheoYeuCau;
    }

    public void setPhongTheoYeuCau(boolean PhongTheoYeuCau) {
        this.PhongTheoYeuCau = PhongTheoYeuCau;
    }

    public BENHNHAN() {
        this.sc =new Scanner(System.in);
    }
    public String getLoaiBaoHiem() {
        return LoaiBaoHiem;
    }

    public void setLoaiBaoHiem(String LoaiBaoHiem) {
        this.LoaiBaoHiem = LoaiBaoHiem;
    }
   
    public BENHNHAN(String LoaiBaoHiem, String MaBenhNhan, String HoTen, Date NgayNhap, boolean PhongTheoYeuCau) {
        this.LoaiBaoHiem = LoaiBaoHiem;
        this.MaBenhNhan = MaBenhNhan;
        this.HoTen = HoTen;
        this.NgayNhap = NgayNhap;
        this.PhongTheoYeuCau = PhongTheoYeuCau;
        this.sc =new Scanner(System.in);
    }   
    public long tinhSoNgayNhapVien(){       
	Calendar calender_Ngayhientai=new GregorianCalendar();
	calender_Ngayhientai.setTime(Calendar.getInstance().getTime());
        Calendar  calendar_Ngaynhapvien=new GregorianCalendar();
	calendar_Ngaynhapvien.setTime(this.NgayNhap);		
	long songaynhapvien=(calender_Ngayhientai.getTimeInMillis()- 
                calendar_Ngaynhapvien.getTimeInMillis())/(1000*60*60*24);		
	return songaynhapvien;        
    } 
    
    public void Nhap(){
        try {
            System.out.println("Nhập mã bệnh nhân:");
            this.MaBenhNhan=sc.nextLine();
            System.out.println("Nhập họ và tên:");
            this.HoTen=sc.nextLine();
          
            System.out.println("Ngày vào viện");
            SimpleDateFormat dayformat=new SimpleDateFormat("dd/MM/yyyy");
            this.NgayNhap=dayformat.parse(sc.nextLine());
          
            System.out.println("loại bảo hiểm  y tế, bảo hiểm xã hội");
            this.LoaiBaoHiem=this.sc.nextLine();
          
            System.out.println("Nhập ký tự 'y' hoặc 'Y' cho phòng theo yêu cầu");
            char yeucau=sc.nextLine().charAt(0);
            if(yeucau=='y' || yeucau=='Y')
                this.PhongTheoYeuCau=true;
            else
                this.PhongTheoYeuCau=false;
        } catch (Exception e) {  }
      
    }
    public void Xuat(){
            System.out.println(" Ma Benh Nhan:"+this.MaBenhNhan);
            System.out.println("Ho ten:"+this.HoTen);
            System.out.println("Ngay Nhap Vien:"+this.NgayNhap.toString());
            if(this.PhongTheoYeuCau)
                System.out.println("Phong theo yeu cau");
            else
                System.out.println("Phong khong theo yeu cau"); 
            
            System.out.println("loại bảo hiểm:"+this.LoaiBaoHiem);
      }
    
   
    
}
