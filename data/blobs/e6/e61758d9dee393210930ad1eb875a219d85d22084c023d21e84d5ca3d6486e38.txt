package com.example.circle.service.impl;

import com.example.circle.mapper.SubjectMapper;
import com.example.circle.model.Subject;
import com.example.circle.service.SubjectService;
import com.example.circle.util.Result;
import com.example.circle.util.ResultUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class SubjectServiceImpl implements SubjectService {

    private final SubjectMapper subjectMapper;

    @Autowired
    public SubjectServiceImpl(SubjectMapper subjectMapper) {
        this.subjectMapper = subjectMapper;
    }

    @Override
    @Transactional(readOnly = true)
    public Result<Subject> getSubjectById(String subjectId) {
        try {
            Subject subject = subjectMapper.getSubjectById(subjectId);
            if (subject == null) {
                return ResultUtil.error("Subject with ID " + subjectId + " not found.");
            }
            return ResultUtil.success(subject);
        } catch (Exception e) {
            return ResultUtil.error("Failed to retrieve subject: " + e.getMessage());
        }
    }

    @Override
    @Transactional
    public Result<Void> insertSubject(Subject subject) {
        try {
            subjectMapper.insertSubject(subject);
            return ResultUtil.success();
        } catch (Exception e) {
            return ResultUtil.error("Failed to insert subject: " + e.getMessage());
        }
    }

    @Override
    @Transactional
    public Result<Void> updateSubject(Subject subject) {
        try {
            int updated = subjectMapper.updateSubject(subject);
            if (updated == 0) {
                return ResultUtil.error("No subject found with ID " + subject.getSubjectId());
            }
            return ResultUtil.success();
        } catch (Exception e) {
            return ResultUtil.error("Failed to update subject: " + e.getMessage());
        }
    }

    @Override
    @Transactional
    public Result<Void> deleteSubject(String subjectId) {
        try {
            String deleted = subjectMapper.deleteSubject(subjectId);
            if (deleted == null) {
                return ResultUtil.error("No subject found with ID " + subjectId);
            }
            return ResultUtil.success();
        } catch (Exception e) {
            return ResultUtil.error("Failed to delete subject: " + e.getMessage());
        }
    }

    @Override
    @Transactional(readOnly = true)
    public Result<List<Subject>> getAllSubjects() {
        try {
            List<Subject> subjects = subjectMapper.getAllSubjects();
            return ResultUtil.success(subjects);
        } catch (Exception e) {
            return ResultUtil.error("Failed to retrieve subjects: " + e.getMessage());
        }
    }

    @Override
    @Transactional(readOnly = true)
    public Result<Subject> getSubjectByNumber(String subjectNumber) {
        try {
            Subject subject = subjectMapper.getSubjectByNumber(subjectNumber);
            if (subject == null) {
                return ResultUtil.error("Subject with number " + subjectNumber + " not found.");
            }
            return ResultUtil.success(subject);
        } catch (Exception e) {
            return ResultUtil.error("Failed to retrieve subject by number: " + e.getMessage());
        }
    }
}