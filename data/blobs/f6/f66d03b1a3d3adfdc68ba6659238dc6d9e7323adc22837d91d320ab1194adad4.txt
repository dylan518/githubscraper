package com.example.ASM_JAVA5.service;

import com.example.ASM_JAVA5.entity.Categories;
import com.example.ASM_JAVA5.repository.CategoriesRepository;
import com.example.ASM_JAVA5.service.serviceImpl.CategoriesServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CategoriesService implements CategoriesServiceImpl {
    @Autowired
    private CategoriesRepository categoriesRepository;


    @Override
    public List<Categories> getList() {
        return categoriesRepository.findAll();
    }

    @Override
    public Categories insert(Categories categories) {
        return categoriesRepository.save(categories);
    }

    @Override
    public boolean delete(int id) {
        categoriesRepository.deleteById(id);
        return true;
    }

    @Override
    public Categories update(Integer id, Categories student) {
        Categories categories = categoriesRepository.findById(student.getId()).orElse(null);
        categories.setName(student.getName());
        categories.setStatus(student.getStatus());
        return categoriesRepository.save(categories);
    }

    @Override
    public Categories findById(int id) {
        return categoriesRepository.findById(id).orElse(null);
    }


}
