package com.mini_project.quiz;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Scanner;

public class Quiz {
	
		public Connection getConnection() {
			Connection con = null;
			try {
				Class.forName("com.mysql.cj.jdbc.Driver");
				con = DriverManager.getConnection("jdbc:mysql://localhost:3306/quiz", "root", "Rms120119978390619197");
				

			} catch (Exception e) {
				
				e.printStackTrace();
			}
					
			return con;
			
		}
		private  void getGrade(int x) {
			if(x>=8 && x<=10) {
				System.out.println("Result: Grade A ");
			}else if(x>=6 &&  x<8) {
				System.out.println("Result: Grade B ");
			}else if(x == 5) {
				System.out.println("Result: Grade C ");
			}else {
				System.out.println("Result: Fail");

			}
		}
		
		private void getStudentData(Connection con) throws Exception {
			Scanner sc2 = new Scanner(System.in);
			System.out.println("Enter the number of students: ");
			int num = sc2.nextInt();
			
			for(int i=1;i<=num;i++) {
				int count = 0;
				PreparedStatement ps = null;
				try {
					ps = con.prepareStatement("Select Question, a, b, c, d,answer from quiz order by rand() limit 10; ");
				
				PreparedStatement ps1 = con.prepareStatement("Select QuestionNo from quiz;");
				ResultSet rs = ps.executeQuery();
				ResultSet rs1 = ps1.executeQuery();
				Scanner sc = new Scanner(System.in);
				System.out.println("Enter the student id of student serial number "+i);
				int id = sc.nextInt();
				System.out.println("Enter the name: ");
				String fullName = sc.next();
				System.out.println("Choose the correct option from given options for each of the following question:");
				

			while(rs.next()) {
				if(rs1.next())
					System.out.println("QuestionNo: "+rs1.getInt(1));
					System.out.println("Question: "+rs.getString(1));
					System.out.println("a) "+rs.getString(2));
					System.out.println("b) "+rs.getString(3));
					System.out.println("c) "+rs.getString(4));
					System.out.println("d) "+rs.getString(5));
						System.out.println("");
					System.out.println("Enter the correct option: ");
					Scanner sc1= new Scanner(System.in);
					String option = sc1.next();
					String ans = rs.getString(6);
					

					if(option.equals(ans)){
						System.out.println("Correct Answer");
							count++;
							System.out.println("");
						
					}else {
						System.out.println("Incorrect Answer");
						System.out.println("");
						
					}
			}
					int x = count;
					System.out.println("Total correct answers are: "+x);
					getGrade(x);
					System.out.println("");
					StoreStudent(con, id, fullName, x);
					
			
				} catch (Exception e) {
					
					e.printStackTrace();
				}
					
			}
			
			
			
			
		}
		
		private void StoreStudent(Connection con, int id, String fullName, int x) throws Exception {
			PreparedStatement ps2 = con.prepareStatement("insert into student(studentId, studentName,score)values(?,?,?);");
			ps2.setInt(1, id);
			ps2.setString(2, fullName);
			ps2.setInt(3, x);
			ps2.executeUpdate();
		}

		private void DisplaySortedScore(Connection con) throws Exception {
			PreparedStatement ps3 = con.prepareStatement("select * from student order by score DESC");
			
			ResultSet rs3 = ps3.executeQuery();
			while(rs3.next()) {
				System.out.println("Student ID: "+rs3.getInt(1));
				System.out.println("Student Name: "+rs3.getString(2));
				System.out.println("Student Score: "+rs3.getInt(3));
				System.out.println("");
			}
			
		}
		
		
		private void DisplayFinalResult(Connection con) throws Exception {
			Scanner sc = new Scanner(System.in);
			System.out.println("Enter Student ID: ");
			int id = sc.nextInt();
			PreparedStatement ps3 = con.prepareStatement("select * from student where studentId = ?;");
			ps3.setInt(1, id);
			ResultSet rs3 = ps3.executeQuery();
			
			while(rs3.next()) {
				System.out.println("Student ID: "+rs3.getInt(1));
				System.out.println("Student Name: "+rs3.getString(2));
				System.out.println("Student Score: "+rs3.getInt(3));
				System.out.println("");
			}
			
		}
		

		public static void main(String[] args) throws Exception {
			
			
			Quiz displayMCQs = new Quiz();
			Connection con =displayMCQs.getConnection();
			displayMCQs.getStudentData(con);
			displayMCQs.DisplaySortedScore(con);
			displayMCQs.DisplayFinalResult(con);
	}
	}



