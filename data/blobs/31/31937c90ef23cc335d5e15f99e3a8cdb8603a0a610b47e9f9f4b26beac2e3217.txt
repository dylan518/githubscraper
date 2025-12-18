package com.example.demo.service;

import com.example.demo.dao.PetRepo;
import com.example.demo.model.Pet;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PetService {

    @Autowired
    PetRepo petRepo;


    public long savePet(Long user_id, String name) {
        return petRepo.savePet(user_id, name);
    }

    public List<Pet> getPets() {
        return petRepo.getPets();
    }
}
