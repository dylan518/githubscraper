package com.ultimate.systems.rekrutacja.service;

import com.ultimate.systems.rekrutacja.DTO.Student;
import com.ultimate.systems.rekrutacja.repository.StudentRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.net.URI;
import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class StudentService {

    final StudentRepository studentRepository;

    public ResponseEntity<Student> save(Student student){

        Student savedStudent = studentRepository.save(student);
        return ResponseEntity.created(URI.create("/api/student/" +savedStudent.getId())).build();
    }

    public ResponseEntity<List<Student>> getAllStudents(){
        List<Student> student = studentRepository.findAll();

        if(student.isEmpty()){
            return ResponseEntity.noContent().build();
        }

        return ResponseEntity.ok(student);
    }

    public ResponseEntity<Long> updateStudent(long id, Student newStudent){
        Optional<Student> studentData = studentRepository.findById(id);

        if(studentData.isPresent()){
            Student tmp = studentData.get();
            tmp.setName(newStudent.getName());
            tmp.setSurname(newStudent.getSurname());
            tmp.setEmail(newStudent.getEmail());
            tmp.setAge(newStudent.getAge());
            tmp.setCourse(newStudent.getCourse());
            tmp.setTeachers(newStudent.getTeachers());

            Student savedTeacher = studentRepository.save(tmp);
            return ResponseEntity.ok(savedTeacher.getId());
        }
        else {
            return ResponseEntity.notFound().build();
        }
    }

    public ResponseEntity<HttpStatus> deleteStudent(long id){
        try{
            studentRepository.deleteById(id);
            return ResponseEntity.noContent().build();
        }catch (Exception e){
            return ResponseEntity.notFound().build();
        }
    }
}
