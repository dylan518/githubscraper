package kln.iad.lms.service;

import kln.iad.lms.dto.CreateEvaluationDto;
import kln.iad.lms.entity.AppUser;
import kln.iad.lms.entity.Course;
import kln.iad.lms.entity.CourseEvaluation;
import kln.iad.lms.repository.EvaluationRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class EvaluationServiceImpl implements EvaluationService{
    @Autowired
    private EvaluationRepo evaluationRepo;

    @Autowired
    AppUserServiceImpl appUserService;

    @Autowired
    CourseService courseService;

    @Override
    public Optional<CourseEvaluation> makeEvaluation(CreateEvaluationDto evaluationInfo) throws Exception {

        Optional<AppUser> lecturer = appUserService.getAppUserById(evaluationInfo.getTeacherId());

        if(lecturer.isEmpty()) {
            throw new Exception("Teacher not found");
        }

        Optional<AppUser> student = appUserService.getAppUserById(evaluationInfo.getStudentId());

        if(student.isEmpty()){
            throw new Exception("Student not found");
        }

        Optional<Course> course = courseService.getCourseById(evaluationInfo.getCourseId());

        if(course.isEmpty()) {
            throw new Exception("Course not found");
        }

        CourseEvaluation evaluation = new CourseEvaluation();
        evaluation.setTeacher(lecturer.get());
        evaluation.setStudent(student.get());
        evaluation.setCourse(course.get());



        return Optional.of(evaluationRepo.save(evaluation));
    }
}
