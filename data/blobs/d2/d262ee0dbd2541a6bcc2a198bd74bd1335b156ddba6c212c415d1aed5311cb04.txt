package com.SpringDataJPA;

import com.SpringDataJPA.model.Student;
import com.SpringDataJPA.repository.StudentRepository;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import java.util.Optional;

@SpringBootApplication
public class SpringDataJpaApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringDataJpaApplication.class, args);
		ApplicationContext context=SpringApplication.run(SpringDataJpaApplication.class,args);

		StudentRepository repo=context.getBean(StudentRepository.class);


		Student s1= context.getBean(Student.class);
		Student s2= context.getBean(Student.class);
		Student s3= context.getBean(Student.class);

		s1.setRollno(1);
		s1.setMarks(21);
		s1.setName("king");

		s2.setRollno(2);
		s2.setMarks(31);
		s2.setName("queen");

		s3.setRollno(3);
		s3.setMarks(41);
		s3.setName("minister");

//		repo.save(s1);
//		repo.save(s2);
//		repo.save(s3);   //Inserts the objects in to the table

		//System.out.println(repo.findAll()); //Prints all the objects to the console
		//System.out.println(repo.count());   //Prints the number of rows in the table.
		//System.out.println(repo.findById(3)); //prints the particular object to the console with id 3. Id is the primary key of table

		Optional<Student> s= repo.findById(3);
		System.out.println(s.orElse(new Student())); //prints the object if present or else prints null object
		//The findById() actually returns a Optional Object which means it may also have a null value if the id is not present
		//So,to handle the null value there is this optional object.

		System.out.println(repo.findByName("queen"));
		System.out.println(repo.findByMarksGreaterThan(40));



	}

}
