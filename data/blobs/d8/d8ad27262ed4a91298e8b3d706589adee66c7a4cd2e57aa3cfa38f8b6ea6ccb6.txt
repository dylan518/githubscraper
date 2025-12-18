package sn.isi.Emploi.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import sn.isi.Emploi.model.Categorie;
import sn.isi.Emploi.service.CategorieService;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/categories")
public class CategorieController {
    @Autowired
    private CategorieService categorieService;

    @PostMapping()
    public ResponseEntity<?> add(@RequestBody Categorie categorie) {
        Categorie categorie1 = categorieService.add(categorie);
        if (categorie1 != null) {
            return new ResponseEntity<>(categorie1, HttpStatus.OK);
        } else
            return new ResponseEntity<>(categorie1, HttpStatus.BAD_REQUEST);
    }

    @GetMapping()
    public ResponseEntity<List<Categorie>> getAll()
    {
        List<Categorie> categorie = categorieService.getAll();
        if (categorie != null) { return new ResponseEntity<>(categorie,HttpStatus.OK); }
        else { return new ResponseEntity<>(HttpStatus.NOT_FOUND); }
    }

    @GetMapping("/{id}")
    public ResponseEntity<Categorie> getCategorie(@PathVariable Integer id) {
        Categorie categorie = categorieService.getCategorie(id);
        if (categorie != null ) { return new ResponseEntity<>(categorie, HttpStatus.OK); }
        else { return new ResponseEntity<>(HttpStatus.NOT_FOUND); }
    }


    @DeleteMapping("/{id}")
    public ResponseEntity<Categorie> deleteById(@PathVariable Integer id)
    {
        categorieService.delete(id);
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Categorie> fullUpdate(@Valid @RequestBody Categorie categorie, @PathVariable Integer id) {
        Categorie oldCat = categorieService.getCategorie(id);
        Categorie newCat = null;

        if (oldCat != null){
            categorie.setId(oldCat.getId());
            newCat = categorieService.update(categorie);

        }
        if (newCat != null){
            return new ResponseEntity<>(newCat, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }
    }


}

