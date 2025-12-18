package quiz;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import java.util.Scanner;

//author by 
public class ClassD {

	public Connection getQuestion() {
		Connection connection = null;

		try {

			// Step 1 Loading the class
			Class.forName("com.mysql.jdbc.Driver");

			// Establish the connection
			connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/miniproject", "root", "Shree@1994");

			// Prepared Statement with select query
			
		 PreparedStatement preparedstatement = connection.prepareStatement("select * from quiz");
		 		
		 
		} catch (Exception e) {
			e.printStackTrace();
		}
		return connection;

	}
	
	// Author by Prajwal_Dharankar

	static int i = 1;

	public void getAnswer() {
		PreparedStatement preparedstatement1 = null;
		ResultSet resulset = null;
		int Score = 0;
		String grade = "";
		System.out.println("Candidate details>>");

		Scanner scanner = new Scanner(System.in);
		System.out.println(" firstname name of candidate>> ");
		String fn = scanner.next();
		System.out.println(" lastname name of candidate>> ");
		String ln = scanner.next();
		System.out.println(
				"---------------------------------------------------------------------------------------------------------");
		System.out.println("Read instruction carefully>>");
		System.out.println("1.choose any one option");
		System.out.println("2.one correct answer get one mark");
		System.out.println("3.write the correct answer in a,b,c,d format for example question 1. ans a");
		System.out.println(
				"---------------------------------------------------------------------------------------------------------");
		System.out.println("Start Quiz>>>>");

		try {
			Connection connection1 = getQuestion();
			preparedstatement1 = connection1.prepareStatement("select * from quiz order by rand()");

			ResultSet resultset = preparedstatement1.executeQuery();

			while (resultset.next()) {

				System.out.println(i + resultset.getString(2));
				i++;
				System.out.println(resultset.getString(3));
				System.out.println(resultset.getString(4));
				System.out.println(resultset.getString(5));
				System.out.println(resultset.getString(6));
				System.out.println("Enter the ans>>");
				String ans1 = scanner.next();
				System.out.println("Ans>> " + ans1);
				if (ans1.equals(resultset.getString(7))) {
					Score++;
				}

			}

			System.out.println();
			// Author by Snehal Dahare

		} catch (Exception e) {
			e.printStackTrace();

		}
		if (Score >= 8 && Score <= 10) {
			grade = "class-A";
		}
		if (Score >= 6 && Score < 8) {
			grade = "class-B";
		}

		if (Score == 5) {
			grade = "class-c";
		}
		if (Score < 5) {
			grade = "fail";
		}
		System.out.println("Total Score>>" + Score);
		Student student = new Student();
		student.getdata(fn, ln, Score, grade);

	}

}
