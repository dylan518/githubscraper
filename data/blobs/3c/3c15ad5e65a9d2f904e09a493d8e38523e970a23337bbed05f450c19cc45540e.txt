package com.citymanager.app.service.impl;

import java.util.List;

import org.springframework.stereotype.Service;

import com.citymanager.app.model.Saving;
import com.citymanager.app.repository.SavingRepository;
import com.citymanager.app.service.ISavingService;

@Service
public class SavingService implements ISavingService{

    private SavingRepository savings;

    public SavingService(SavingRepository sr) {
        super();
        this.savings = sr;
    }

    @Override
    public Saving findbyId(long id) {
        try {
            return this.savings.findById(id).get();
        } catch (Exception e) {
            return null;
        }
    }

    @Override
    public List<Saving> findAll() {
        return this.savings.findAll();
    }

    @Override
    public boolean delete(long id) {
        Saving s = this.findbyId(id);
        try {
            this.savings.delete(s);
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    @Override
    public Saving create(Saving s) {
        s = this.savings.save(s);
        return s;
    }



    @Override
    public Saving update(long id, Saving fromData) {
        Saving oldSaving = this.findbyId(id);

        if (oldSaving == null) {
            return null;
        }

        oldSaving.setPurposeOfSaving(fromData.getPurposeOfSaving());

        return this.savings.save(oldSaving);
    }

    
    
}
