package com.example.test;

import com.example.test.model.Address;
import com.example.test.model.Gender;
import com.example.test.model.Student;
import com.example.test.repo.StudentReposotry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.time.ZonedDateTime;
import java.util.List;

@SpringBootApplication
public class TestApplication implements CommandLineRunner  {
	@Autowired
	StudentReposotry studentReposotry;

	public static void main(String[] args) {
		SpringApplication.run(TestApplication.class, args);
	}


	@Bean
	public CommandLineRunner runner(StudentReposotry reposotry, MongoTemplate mongoTemplate){

		return args -> {
			String  email="amani@gmail.com";
			Address address=new Address("tunisia","tunis","10000");
			Student student =new Student("amani",
					"akremi",
					email,
					Gender.FEMALE,
					address,
					List.of("intellegence artefecielle"),
					BigDecimal.TEN,
					LocalDateTime.now());
			//usingmongodbTemplateQuerry(reposotry, mongoTemplate, email, student);
			reposotry.findStudentByEmail(email).ifPresentOrElse(
					s->{System.out.println("student==>  "+ s + "is exist");},
			()->{reposotry.insert(student);}
			);
		};
	}

	private  void usingmongodbTemplateQuerry(StudentReposotry reposotry, MongoTemplate mongoTemplate, String email, Student student) {
		Query query =new Query();
		query.addCriteria(Criteria.where("email").is(email));
		List<Student> students = mongoTemplate.find(query, Student.class);

		if (students.size()>=1){
			System.out.println("email"+ email + "is exist");
		}else{
			reposotry.insert(student);

		}
	}


	@Override
	public void run(String... args) throws Exception {

	}
}
