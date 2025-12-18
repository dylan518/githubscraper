package com.ltp.gradesubmission;

import com.ltp.gradesubmission.pojo.Grade;
import com.ltp.gradesubmission.repository.GradeRepository;
import com.ltp.gradesubmission.service.GradeService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnitRunner;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@RunWith(MockitoJUnitRunner.class)
public class GradeServiceTest {
    @Mock
    private GradeRepository gradeRepository;

    @InjectMocks
    private GradeService gradeService;

    // Usually you would not test something like getGrades as it is trivial
    @Test
    public void getGradesFromRepoTest() {
        when(gradeRepository.getGrades()).thenReturn(Arrays.asList(
                new Grade("Harry", "Potions", "A-"),
                new Grade("Harry", "DADA", "A+"),
                new Grade("Harry", "Potions", "A-")
        ));
        List<Grade> result = gradeService.getGrades();

        assertEquals("Harry", result.get(0).getName());
        assertEquals("DADA", result.get(1).getSubject());
    }

    @Test
    public void getGradeIndexTest() {
        Grade grade = new Grade("Harry", "Potions", "A-");
        when(gradeRepository.getGrades()).thenReturn(Arrays.asList(grade
        ));
        when(gradeRepository.getGrade(0)).thenReturn(grade);
        List<Grade> result = gradeService.getGrades();
        int valid = gradeService.getGradeIndex(result.get(0).getId());
        int notFound = gradeService.getGradeIndex("123");

        assertEquals(0, valid);
        assertEquals(Constants.NOT_FOUND, notFound);
    }

    @Test
    public void returnGradeByIdTest() {
        Grade grade = new Grade("Harry", "Potions", "A-");
        when(gradeRepository.getGrades()).thenReturn(Arrays.asList(grade
        ));
        when(gradeRepository.getGrade(0)).thenReturn(grade);

        String id = grade.getId();
        Grade result = gradeService.getGradeById(id);
        assertEquals(grade, result);
    }
    @Test
    public void submitGradeTest(){
        Grade grade = new Grade("Harry", "Potions", "A-");
        when(gradeRepository.getGrades()).thenReturn(Arrays.asList(grade
        ));
        when(gradeRepository.getGrade(0)).thenReturn(grade);

        Grade newGrade = new Grade("Ramaj", "JS", "A+");
        gradeService.submitGrade(newGrade);

        verify(gradeRepository, times(1)).addGrade(newGrade);
    }
    @Test
    public void updateGradeTest(){
        Grade grade = new Grade("Harry", "Potions", "A-");
        when(gradeRepository.getGrades()).thenReturn(Arrays.asList(grade
        ));
        when(gradeRepository.getGrade(0)).thenReturn(grade);

        grade.setScore("B+");
        gradeService.submitGrade(grade);

        verify(gradeRepository, times(1)).updateGrade(grade, 0);
    }
} // Test class
