package com.karthik.springjpaex;

import com.karthik.springjpaex.model.Student;
import com.karthik.springjpaex.service.StudentService;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class SpringJpaExApplication {

	public static void main(String[] args) {

		ApplicationContext context=SpringApplication.run(SpringJpaExApplication.class, args);

		/* Note:f you want to enable below line use @Component annotation
		at Student Class use Model Package along with @Entity Annotation*/
		//Student student = context.getBean(Student.class);

		Student student = new Student();
		student.setId(101);
		student.setName("Ganesh");
		student.setAge(5);

		StudentService studentService=context.getBean(StudentService.class);
		//studentService.save(student);
		System.out.println(studentService.getStudents());


	}

}
