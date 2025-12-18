package org.aposternak35.app.controller;

import org.aposternak35.app.domain.Mark;
import org.aposternak35.app.domain.Model;
import org.aposternak35.app.domain.Modification;
import org.aposternak35.app.service.MarkService;
import org.aposternak35.app.service.ModelService;
import org.aposternak35.app.service.ModificationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.NoSuchElementException;

@RestController
public class ModelController {
    @Autowired
    ModelService modelService;
    @Autowired
    ModificationService modificationService;

    @GetMapping("/model")
    public List<Model> getAllModels(){
        return modelService.getAll();
    }
    @GetMapping("/model/{uid}")
    public Model getModelById(@PathVariable long uid){
        return modelService.getById(uid);
    }

    @GetMapping("/model/{uid}/modification")
    public List<Modification> getAllModifications(@PathVariable long uid){
        return modelService.getById(uid).getModifications();
    }

    @GetMapping("/model/{modelId}/modification/{modificationId}")
    public Modification getModificationById(@PathVariable long modelId,@PathVariable long modificationId){
        for (Modification modification:modelService.getById(modelId).getModifications()){
            if(modification.getUid()==modificationId){
                return modification;
            }
        }
        throw new NoSuchElementException();
    }

    @PostMapping("/model")
    public Model saveModel(@RequestBody Model model){
        modelService.saveOrUpdate(model);
        return model;
    }

    @PostMapping("/model/{uid}/modification")
    public Modification saveModification(@PathVariable long uid,@RequestBody Modification modification){
        modelService.getById(uid).getModifications().add(modification);
        modification.setModel(modelService.getById(uid));
        modificationService.saveOrUpdate(modification);
        return modification;
    }
}
