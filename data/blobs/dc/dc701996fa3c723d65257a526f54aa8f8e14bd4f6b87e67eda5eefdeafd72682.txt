package automation.testsuite;

import java.util.Scanner;

import org.testng.annotations.*;

public class Login {

@BeforeMethod
 public void init ()
 {
	System.out.print(" beforeMethod");
 }
@Test
public void testcase1()
{
	System.out.print(" testcase1");
}
@Test
public void NhanVien ()
{
    
        Scanner scanner = new Scanner(System.in);

        System.out.print("Nhập số lượng nhân viên: ");
        int soLuong = scanner.nextInt();
        scanner.nextLine();


        String[] danhSachNhanVien = new String[soLuong];

        for (int i = 0; i < soLuong; i++) {
            System.out.print("Nhập tên nhân viên " + (i + 1) + ": ");
            danhSachNhanVien[i] = scanner.nextLine();
        }
        System.out.println("Danh sách tên nhân viên:");
        for (String ten : danhSachNhanVien) {
            System.out.println(ten);
        }

        scanner.close();
    }
}

