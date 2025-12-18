package edu.mimo.InVinoVeritas.rest;

import edu.mimo.InVinoVeritas.model.TypeDeVin;
import edu.mimo.InVinoVeritas.service.TypeDeVinService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/typedevin")
public class TypeDeVinController {

    @Autowired
    private TypeDeVinService typeDeVinService;

    @GetMapping
    public List<TypeDeVin> getAllTypeDeVins() {
        return typeDeVinService.allTypeDeVins();
    }

    @GetMapping("/{id}")
    public ResponseEntity<TypeDeVin> getTypeDeVinById(@PathVariable Integer id) {
        Optional<TypeDeVin> typeDeVin = typeDeVinService.rechercheTypeDeVinParId(id);
        return typeDeVin.map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @GetMapping("/recherche")
    public List<TypeDeVin> getTypeDeVinByName(@RequestParam String nom) {
        return typeDeVinService.rechercheTypeDeVinsParNom(nom);
    }

    @PostMapping
    public TypeDeVin createTypeDeVin(@RequestBody TypeDeVin typeDeVin) {
        return typeDeVinService.enregistreTypeDeVin(typeDeVin);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteTypeDeVin(@PathVariable Integer id) {
        typeDeVinService.supressionTypeDeVinParId(id);
        return ResponseEntity.noContent().build();
    }
}
