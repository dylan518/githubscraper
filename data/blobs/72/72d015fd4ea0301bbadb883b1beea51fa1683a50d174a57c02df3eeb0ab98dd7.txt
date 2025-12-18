package MavenFun.MavenFun1;

import java.util.Scanner;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class AddStudent {

	public static void main(String[] args) {
		// Initialize SessionFactory

		Scanner scanner = new Scanner(System.in);

		System.out.print("Enter student name: ");
		String Stud_Name = scanner.nextLine();

		System.out.print("Enter student age: ");
		int Stud_Age = scanner.nextInt();

		// Create student object with user input
		Student stud = new Student(Stud_Name, Stud_Age);
		Configuration conf = new Configuration();
		conf.configure("hibernate.cfg.xml");
		SessionFactory sef = conf.buildSessionFactory();
		Session session = sef.openSession();
		Transaction transaction = session.beginTransaction(); // Start the transaction
		session.persist(stud);
		transaction.commit(); // Commit the transaction
		System.out.println("Student added successfully!");
		session.close(); // Close the session
		// Open a session and begin a transaction

		scanner.close();
	}

}
