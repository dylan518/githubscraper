package com.projects.springbootuniversity.service;

import com.projects.springbootuniversity.entity.Professor;
import com.projects.springbootuniversity.repository.ProfessorRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProfessorServiceImpl implements ProfessorService{

    private final ProfessorRepository repository;

    public ProfessorServiceImpl(final ProfessorRepository repository){
        this.repository = repository;
    }

    @Override
    public Professor saveProfessorToUniversityDB(Professor professor) {
        return this.repository.save(professor);
    }

    @Override
    public List<Professor> getAllProfessorFromUniversityDB() {
        return this.repository.findAll();
    }
}
