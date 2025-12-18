package com.TodoApplication.App.Controller;

import com.TodoApplication.App.Model.Role;
import com.TodoApplication.App.Service.RoleService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api")
public class RoleController {

    @Autowired
    private RoleService roleService;

    @PostMapping("/admin/addRole")
    public ResponseEntity<Role> addRole(@Valid @RequestBody Role role){
        return new ResponseEntity<>(roleService.createRole(role), HttpStatus.CREATED);
    }

    @GetMapping("/getAllRoles")
    public ResponseEntity<List<Role>> getAllRoles(){
        return new ResponseEntity<>(roleService.getAllRoles(),HttpStatus.OK);
    }

    @GetMapping("/getRole/{id}")
    public ResponseEntity<Role> getRoleById(@PathVariable Long id){
        return new ResponseEntity<>(roleService.getRoleById(id),HttpStatus.OK);
    }
}
