package com.example.agroltec.Controller;

import com.example.agroltec.Model.Productos;
import com.example.agroltec.Repository.ProductoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.List;

@RestController
@RequestMapping("/tienda/inventario/productos")
@CrossOrigin(origins = "http://localhost:8081")
public class ProductoController {

    @Autowired
    private ProductoRepository repository;


    @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public List<Productos> getAllProducts() {
        return repository.findAll();
    }


    @PostMapping(consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity addProduct(@RequestBody Productos nueva) throws URISyntaxException {
        Productos factura = repository.save(nueva);
        return ResponseEntity.created(new URI("/factura/" + factura.getId())).body(factura);
    }

    @GetMapping(path = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public Productos getProduct(@PathVariable Integer id) {
        return repository.findById(id).get();
    }

    @PutMapping(path = "/{id}")
    public ResponseEntity updateProduct(@PathVariable Integer id, @RequestBody Productos producto) {
        Productos updateBill = repository.findById(id).orElseThrow(RuntimeException::new);
        repository.save(producto);
        return ResponseEntity.ok(producto);
    }

    @DeleteMapping(path = "/{id}")
    public ResponseEntity deleteProduct(@PathVariable Integer id) {
        repository.deleteById(id);
        return ResponseEntity.ok().build();
    }

}
