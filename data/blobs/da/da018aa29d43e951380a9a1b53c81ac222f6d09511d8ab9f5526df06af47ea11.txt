package kiet.edu.project.canteen_connect.controllers;

import java.net.URI;
import java.util.HashMap;
import java.util.Map;

import kiet.edu.project.canteen_connect.models.User;
import kiet.edu.project.canteen_connect.services.UserDetailsServiceImpl;
import kiet.edu.project.canteen_connect.services.UserService;
import kiet.edu.project.canteen_connect.utils.JwtUtil;
import lombok.RequiredArgsConstructor;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;


@RequestMapping("/api/v1/users")
@RestController
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;
    private final AuthenticationManager authenticationManager;
    private final JwtUtil jwtUtil;
    private final UserDetailsServiceImpl userDetailsServiceImpl;

    @GetMapping
    public ResponseEntity<?> registerUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        User user = userService.findConsumerByEmail(authentication.getName());
        return ResponseEntity.ok().body(user);
    }

    @PostMapping("/register")
    public ResponseEntity<?> registerUser(@RequestBody User newUser) {
        User savedUser = userService.createConsumer(newUser);
        URI location = ServletUriComponentsBuilder
                .fromCurrentRequest()
                .path("/{userEmail}")
                .buildAndExpand(savedUser.getEmail())
                .toUri();
        return ResponseEntity.created(location).build();
    }

    @PostMapping("/login")
    public ResponseEntity<?> loginUser(@RequestBody User user) {
        Authentication authentication = authenticationManager
                .authenticate(new UsernamePasswordAuthenticationToken(user.getEmail(), user.getPassword()));
        if (authentication.isAuthenticated()) {
            Map<String, String> authResponse = new HashMap<>();
            authResponse.put("token", jwtUtil.generateToken(userDetailsServiceImpl.loadUserByUsername(
                    user.getEmail())));
            return new ResponseEntity<>(authResponse.toString(), HttpStatus.OK);
        }
        throw new UsernameNotFoundException("Invalid credentials");
    }


    @PutMapping
    public ResponseEntity<?> updateUser(@RequestBody User user) {
        User updatedUser = userService.updateUser(user);
        return ResponseEntity.ok().body(updatedUser);
    }

    @DeleteMapping
    public ResponseEntity<?> deleteUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        userService.deleteByUserName(authentication.getName());
        return new ResponseEntity<>(HttpStatus.NO_CONTENT);
    }
}
