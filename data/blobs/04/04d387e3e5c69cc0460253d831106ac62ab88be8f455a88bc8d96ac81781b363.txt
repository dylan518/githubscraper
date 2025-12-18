package com.example.brussel.be.mockito_tests;

import com.example.brussel.be.model.Diagnose;
import com.example.brussel.be.repository.DiagnoseRepository;
import com.example.brussel.be.service.DiagnoseService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

@SpringBootTest
public class DiagnoseServiceTest {

    @Autowired
    private DiagnoseService diagnoseService;

    @MockBean
    private DiagnoseRepository diagnoseRepository;

    @Test
    public void testGetAllDiagnoses() {
        Diagnose diagnose1 = new Diagnose(1L, "ICD1", "Diagnose1", "Description1", null);
        Diagnose diagnose2 = new Diagnose(2L, "ICD2", "Diagnose2", "Description2", null);

        when(diagnoseRepository.findAll()).thenReturn(Arrays.asList(diagnose1, diagnose2));

        List<Diagnose> diagnoses = diagnoseService.getAllDiagnoses();

        assertEquals(2, diagnoses.size());
        assertEquals(diagnose1, diagnoses.get(0));
        assertEquals(diagnose2, diagnoses.get(1));

        verify(diagnoseRepository, times(1)).findAll();
    }

    @Test
    public void testGetDiagnoseById() {
        Diagnose diagnose = new Diagnose(1L, "ICD1", "Diagnose1", "Description1", null);

        when(diagnoseRepository.findById(1L)).thenReturn(Optional.of(diagnose));

        Optional<Diagnose> result = diagnoseService.getDiagnoseById(1L);

        assertEquals(diagnose, result.orElse(null));

        verify(diagnoseRepository, times(1)).findById(1L);
    }
}