package jpa.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody; //
import org.springframework.web.bind.annotation.RestController;

import jpa.entitymodels.User;
import jpa.entitymodels.UserRegistrationRequest;
import jpa.service.UserService;

@RestController
public class RegistrationController {

    @Autowired
    private UserService userService;

    @PostMapping("/register")
    public ResponseEntity<String> registerUser(@RequestBody UserRegistrationRequest request) {
        User user = new User();
        user.setName(request.getName());
        user.setEmail(request.getEmail());
        user.setPassword(request.getPassword());

        userService.registerUser(user);

        return ResponseEntity.ok("Registration successful");
    }
}

