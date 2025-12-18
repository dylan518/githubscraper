package me.dio.demo.controllers;

import jakarta.validation.Valid;
import me.dio.demo.infra.security.TokenService;
import me.dio.demo.models.user.AuthenticationDTO;
import me.dio.demo.models.user.LoginResponseDTO;
import me.dio.demo.models.user.User;
import me.dio.demo.models.user.UserRequestDTO;
import me.dio.demo.repository.UserReposity;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("auth")
public class AuthenticationController {

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private UserReposity userReposity;

    @Autowired
    private TokenService tokenService;

    @PostMapping("/login")
    public ResponseEntity login(@RequestBody @Valid AuthenticationDTO data ){
        var userNamePassword = new UsernamePasswordAuthenticationToken(data.login(), data.password());
        var auth = this.authenticationManager.authenticate(userNamePassword);
        var token = tokenService.generateToken((User) auth.getPrincipal());
        return ResponseEntity.ok(new LoginResponseDTO(token));
    }

    @PostMapping("/register")
    public ResponseEntity register(@RequestBody @Valid UserRequestDTO data){
        if(this.userReposity.findByLogin(data.login()) != null){
            return ResponseEntity.badRequest().build();
        }
        String encriptedPassword = new BCryptPasswordEncoder().encode(data.password());

        User newUser = new User(
                data.name(),
                data.cpf(),
                data.login(),
                encriptedPassword,
                data.role(),
                data.email()
        );

        this.userReposity.save(newUser);
        return ResponseEntity.ok().build();
    }
}
