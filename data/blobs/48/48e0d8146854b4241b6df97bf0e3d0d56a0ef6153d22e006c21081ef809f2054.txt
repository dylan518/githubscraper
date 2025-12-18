package com.vamsi.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DeleteDoctorsDao {
	public boolean deletebyid(int did) {

		boolean flag = false;

		try {
			String query = "DELETE FROM doctors WHERE did = ?";

			Class.forName("com.mysql.cj.jdbc.Driver");
			Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/jdbc", "root", "Vamsi2511@");
			PreparedStatement st = con.prepareStatement(query);
			st.setInt(1, did);
			st.executeUpdate();
			
			flag=true;
		} 
		catch (SQLException ex) {
		    System.out.println("SQL Exception: " + ex.getMessage());
		    ex.printStackTrace();
		} 
		catch (ClassNotFoundException e) {
		    System.out.println("Class Not Found Exception: " + e.getMessage());
		    e.printStackTrace();
		} 
		catch (Exception exception) {
		    System.out.println("Exception: " + exception.getMessage());
		    exception.printStackTrace();
		}

		return flag;
	}
}
