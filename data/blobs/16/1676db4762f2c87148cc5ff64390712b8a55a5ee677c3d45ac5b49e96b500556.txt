package com.iiitb.esdMiniProject.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.iiitb.esdMiniProject.dto.CourseDTO;
import com.iiitb.esdMiniProject.entities.Course;
import com.iiitb.esdMiniProject.repository.CourseRepository;

@Service
public class CourseService {
    
    @Autowired
    private CourseRepository courseRepository;

    public CourseDTO getCourseDetails(String courseCode){
        CourseDTO courseDTO = new CourseDTO();
        Optional<Course> cOptional = courseRepository.findByCourseCode(courseCode);
        if(cOptional.isPresent()){
            Course course = cOptional.get();
            courseDTO.setCourseCode(course.getCourseCode());
            courseDTO.setCourseName(course.getCourseName());
            courseDTO.setTa(course.getTa());
        }
        return courseDTO;
    }
}
