package com.chary.springboot.service;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.chary.springboot.entities.Student;
import com.chary.springboot.repository.StudentRepository;

@Service
public class StudentServiceImpl implements StudentService{
	
	@Autowired
	private StudentRepository studentRepository;

	@Override
	public Student createStudent(Student student) {
		
		return studentRepository.save(student);
	}

	@Override
	public Student getStudentById(int id) {
		
		return studentRepository.findById(id).get();
	}

	@Override
	public List<Student> getAllstudents() {
		
		return studentRepository.findAll();
	}

	@Override
	public Student updateStudentById(Student student, int id) {
		Student updateStudent=studentRepository.findById(id).get();
		updateStudent.setName(student.getName());
		return studentRepository.save(updateStudent) ;
	}

	@Override
	public void deleteById(int id) {
	
	 studentRepository.deleteById(id);
	}
	

}
