
package com.misiontic.proyectociclo3.Controller;

import com.misiontic.proyectociclo3.Models.Cliente;
import com.misiontic.proyectociclo3.service.ClienteService;
import java.util.List;

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

@RestController
@CrossOrigin("*")
@RequestMapping("/cliente")
public class ClienteController {
    @Autowired
    private ClienteService clienteservice;
    
    @PostMapping(value="/")
    public ResponseEntity<Cliente> agregar(@RequestBody Cliente cliente){        
        Cliente obj = clienteservice.save(cliente);
        return new ResponseEntity<>(obj, HttpStatus.OK);     
    }
   
    @DeleteMapping(value="/{id}") 
    public ResponseEntity<Cliente> eliminar(@PathVariable Integer id){ 
        Cliente obj = clienteservice.findById(id); 
        if(obj!=null) 
            clienteservice.delete(id); 
        else 
            return new ResponseEntity<>(obj, HttpStatus.INTERNAL_SERVER_ERROR); 
        return new ResponseEntity<>(obj, HttpStatus.OK); 
    }
    
    @PutMapping(value="/") 
    public ResponseEntity<Cliente> editar(@RequestBody Cliente cliente){ 
        Cliente obj = clienteservice.findById(cliente.getId_cliente()); 
        if(obj!=null) { 
            obj.setNombre(cliente.getNombre());
            obj.setDireccion(cliente.getDireccion());
            obj.setTelefono(cliente.getTelefono());
            obj.setCiudad(cliente.getCiudad());
            clienteservice.save(obj); 
        } 
        else 
            return new ResponseEntity<>(obj, HttpStatus.INTERNAL_SERVER_ERROR); 
        return new ResponseEntity<>(obj, HttpStatus.OK); 
    }
    
    @GetMapping("/list") 
    public List<Cliente> consultarTodo(){
        return clienteservice.findAll(); 
    }
    
    @GetMapping("/list/{id}") 
    public Cliente consultaPorId(@PathVariable Integer id){ 
        return clienteservice.findById(id); 
    }
}
