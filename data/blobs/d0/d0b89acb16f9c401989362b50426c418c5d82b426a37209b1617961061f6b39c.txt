package com.alperarslan.springframeworkspgpetclinic.controllers;

import com.alperarslan.springframeworkspgpetclinic.model.Vet;
import com.alperarslan.springframeworkspgpetclinic.services.VetService;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.Set;

@Controller
public class VetController {
    private final VetService vetService;

    public VetController(VetService vetService) {
        this.vetService = vetService;
    }

    @GetMapping({"/vets","/vets/index","/vets/index.html","/vets.html"})
    public String listVets(Model model){

        model.addAttribute("vets",vetService.findAll());

        return "vets/index";
    }

    @GetMapping("/api/vets")
    public ResponseEntity<Set<Vet>> getVetsJson(){
        return ResponseEntity.ok(vetService.findAll());
    }
}
