package com.devcamp.api.task_64dot30_crud_drinks.controllers;

import java.util.Date;
import java.util.List;
import java.util.Optional;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.web.bind.annotation.RestController;

import com.devcamp.api.task_64dot30_crud_drinks.models.CDrink;
import com.devcamp.api.task_64dot30_crud_drinks.services.CDrinkService;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/api")
@CrossOrigin
public class CDrinkController {
    @Autowired
    CDrinkService pDrinkService;

    @GetMapping("/drinks")
    public ResponseEntity<List<CDrink>> getAllDrink() {
        try {
            return new ResponseEntity<List<CDrink>>(pDrinkService.getAllDrinks(), HttpStatus.OK);
        } catch (Exception e) {
            // TODO: handle exception
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @GetMapping("/drinks/{id}")
    public ResponseEntity<CDrink> getDrinkById(@PathVariable("id") long id) {
        try {
            Optional<CDrink> optionalDrink = pDrinkService.getDrinkById(id);
            if (optionalDrink.isPresent()) {
                return new ResponseEntity<CDrink>(optionalDrink.get(), HttpStatus.OK);
            } else {
                return new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
            }
        } catch (Exception e) {
            // TODO: handle exception
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @PostMapping("/drinks")
    public ResponseEntity<CDrink> createDrink(@Valid @RequestBody CDrink drink) {
        try {
            CDrink newDrink = new CDrink();
            newDrink.setMaNuocUong(drink.getMaNuocUong());
            newDrink.setTenNuocUong(drink.getTenNuocUong());
            newDrink.setDonGia(drink.getDonGia());
            newDrink.setGhiChu(drink.getGhiChu());
            newDrink.setNgayTao(new Date());

            newDrink = pDrinkService.createVoucher(newDrink);
            return new ResponseEntity<CDrink>(newDrink, HttpStatus.OK);
        } catch (Exception e) {
            // TODO: handle exception
            return new ResponseEntity<CDrink>(HttpStatus.NO_CONTENT);
        }
    }

    @PutMapping("/drinks/{id}")
    public ResponseEntity<CDrink> updateDrink(@Valid @PathVariable("id") long id, @RequestBody CDrink drink) {
        try {
            Optional<CDrink> optionalDrink = pDrinkService.getDrinkById(id);
            if (optionalDrink.isPresent()) {
                CDrink updateDrink = optionalDrink.get();
                updateDrink.setMaNuocUong(drink.getMaNuocUong());
                updateDrink.setTenNuocUong(drink.getTenNuocUong());
                updateDrink.setDonGia(drink.getDonGia());
                updateDrink.setGhiChu(drink.getGhiChu());
                updateDrink.setNgayCapNhat(new Date());

                updateDrink = pDrinkService.updateDrink(updateDrink);
                return new ResponseEntity<CDrink>(updateDrink, HttpStatus.OK);
            } else {
                return new ResponseEntity<CDrink>( HttpStatus.NO_CONTENT);
            }
        } catch (Exception e) {
            return new ResponseEntity<CDrink>( HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }

    @DeleteMapping("/drinks/{id}")
    public ResponseEntity<String> deleteDrink(@PathVariable("id") long id) {
        try {
            pDrinkService.deleteDrinkById(id);
            return new ResponseEntity<String>("Da xoa thanh cong", HttpStatus.OK);
        } catch (Exception e) {
            // TODO: handle exception
            return new ResponseEntity<String>(HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}
