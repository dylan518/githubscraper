package com.crud;

import java.sql.*;
import java.util.Scanner;

public class DeleteClass {

    Scanner sc = new Scanner(System.in);
    Connection con = DBClass.createConnection();
    Statement st;

    private int rollno;

    public void deleteData() {

        System.out.println("\t\t\t DELETE THE STUDENT RECORDS : \n");
        System.out.println("Enter Student Roll Number To Be Deleted :");
        rollno = sc.nextInt();
        System.out.println();

        try {

            System.out.println("Are You Sure Want To Delete The Record ?\n");
            System.out.println("If yes type [Yes] otherwise type any letter .");
            String ch = sc.next();

            if (ch.equals("YES") || ch.equals("yes")) {

                st = con.createStatement();

                String sql = "delete from student where rollno = '" + rollno + "'";

                int i = st.executeUpdate(sql);

                if (i == 1) {
                    System.out.println("\nRECORD DELETED SUCCESSFULLY.......");
                } else {
                    System.out.println("No such a record find !");
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

    }

}
