package com.euler.project;

import com.euler.project.repositories.Algorithm;
import com.euler.project.repositories.LargestPrimeFactor;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ProjectApplication {

	public static void main(String[] args) {
		SpringApplication.run(ProjectApplication.class, args);
		Algorithm algorithm = new LargestPrimeFactor();
		int result = algorithm.execute(600851475143L);
		System.out.print("El resultado del ejercicio es: " + result);
	}

}
