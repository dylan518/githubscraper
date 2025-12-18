package com.example.springboot.Module6_JPAandHibernate;

import com.example.springboot.Module6_JPAandHibernate.a1JSpringDBC.CourseJDBCRepository;
import com.example.springboot.Module6_JPAandHibernate.a2JPA.CourseJpaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class CoureCommandlineRunner implements CommandLineRunner {
//    @Autowired
//    private CourseJDBCRepository repository;

    @Autowired
    private CourseJpaRepository repository;


    @Override
    public void run(String... args) throws Exception {
        repository.insert(new Course(1,"Learn SpringBoot","Udemy"));
        repository.insert(new Course(2,"Learn AWS","Udemy"));
        repository.insert(new Course(3,"Learn Kafka","Udemy"));

        repository.deleteById(1);
        System.out.println(repository.selectById(2));
    }
}
