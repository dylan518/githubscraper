package com.lambda.dao;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import com.lambda.models.Student;

import jakarta.annotation.PostConstruct;

@Repository
public class StudentDAO {
    @Autowired
    JdbcTemplate jdbcTmp;

    public StudentDAO() {

    }

    @PostConstruct
    public void createTables() {
        String query = "create table if not exists students( id varchar(36) primary key, full_name varchar(127), gender enum(\"MALE\", \"FEMALE\"), contact varchar(10), address varchar(127), status enum(\"ACTIVE\" , \"INACTIVE\"), dob date, doj date, dol date );";
        int code = jdbcTmp.update(query);
        if (code != 0) {
            System.out.println("Student table created");
        } else {
            System.out.println("Student table already exists code: " + code);
        }
        code = jdbcTmp.update(
                "create table if not exists student_course( student_id varchar(36), course_id varchar(36), earned_credits tinyint, status enum(\"PASS\", \"FAIL\"), foreign key (student_id) references students(id), foreign key (course_id) references courses(id) );");
        if (code != 0) {
            System.out.println("Student-Course table created");
        } else {
            System.out.println("Student-Course table already exists code: " + code);
        }
    }

    public List<Student> getAllStudents() {
        List<Student> students = null;
        try {
            students = jdbcTmp.query("select * from students", new BeanPropertyRowMapper<Student>(Student.class));
        } catch (DataAccessException exp) {
            System.out.println("Error: " + exp.getMessage());
        }
        return students;
    }

    public String[] createStudent(Student student) {
        String[] resp = new String[2];
        try {
            String query = "insert into students (id, full_name, gender, contact, status, address, dob, doj, dol, email) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
            jdbcTmp.update(query, student.getId(), student.getFullName(), student.getGender().name(),
                    student.getContact(), student.getStatus().name(), student.getAddress(), student.getDob(), student.getDoj(), student.getDol(), student.getEmail());
            resp[0] = "msg";
            resp[1] = "New Student Registered!";
        } catch (DataAccessException exp) {
            System.out.println("Error: " + exp.getMessage());
            resp[0] = "err";
            resp[1] = exp.getMessage();
        }
        return resp;
    }

    public Student getSudentById(String id) {
        Student student = null;
        try {
            student = jdbcTmp.queryForObject("select * from student where guId = ?",
                    new BeanPropertyRowMapper<>(Student.class), id);
        } catch (DataAccessException exp) {
            System.out.println("Error: " + exp.getMessage());
        }
        return student;
    }
}
