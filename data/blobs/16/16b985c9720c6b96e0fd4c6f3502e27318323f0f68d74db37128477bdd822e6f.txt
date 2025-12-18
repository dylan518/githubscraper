package ftn.ticketX.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import ftn.ticketX.dto.UserCredentials;
import ftn.ticketX.dto.UserDTO;
import ftn.ticketX.model.Customer;
import ftn.ticketX.security.JwtTokenUtil;
import ftn.ticketX.security.MyUserDetailsService;
import ftn.ticketX.service.UserService;

@RestController
public class AuthenticationController {

	@Autowired
	private AuthenticationManager authenticationManager;
	
	@Autowired
	private MyUserDetailsService myUserDetailsService;
	
	@Autowired
	private JwtTokenUtil jwtTokenUtil;
	
	@Autowired
	private PasswordEncoder passwordEncoder;
	
	@Autowired
	private UserService userService;
	
	@CrossOrigin(origins = "http://localhost:4200")
	@PostMapping("/login")
	public ResponseEntity<?> login(@RequestBody UserCredentials credentials) throws Exception { 
		try {
			authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(credentials.getUsername(), credentials.getPassword()));
		} catch (BadCredentialsException e) {
			e.printStackTrace();
			throw new Exception("Incorect username or password", e);
		}
		
		final UserDetails userDetails = myUserDetailsService.loadUserByUsername(credentials.getUsername());
		
		final String jwt = jwtTokenUtil.generateToken(userDetails);
		
		
		return ResponseEntity.ok(jwt);
	}
	
	@PostMapping("/register")
	public ResponseEntity<?> register(@RequestBody UserDTO userDto) {
		Customer c = new Customer(userDto);
		// encode password first
		c.setPassword(passwordEncoder.encode(c.getPassword()));
		
		userService.saveNewUser(c);
		
		return ResponseEntity.ok().build();	
	}
}
