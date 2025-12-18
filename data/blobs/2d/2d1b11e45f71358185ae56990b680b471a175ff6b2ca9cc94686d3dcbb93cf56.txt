package com.elwgomes.dslist.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.elwgomes.dslist.dto.GameDTO;
import com.elwgomes.dslist.dto.GameMinDTO;
import com.elwgomes.dslist.services.GameService;

@RestController
@RequestMapping(value = "/games")
public class GameController {

    @Autowired
    private GameService gameService;
    
    @GetMapping
    public List<GameMinDTO> findAll () {
        List<GameMinDTO> list = gameService.findAll();
        return list;
    }
    
    @GetMapping(value = "/{id}")
    public GameDTO findById (@PathVariable Long id) {
        GameDTO result = gameService.findById(id);
        return result;
    }
    
}
