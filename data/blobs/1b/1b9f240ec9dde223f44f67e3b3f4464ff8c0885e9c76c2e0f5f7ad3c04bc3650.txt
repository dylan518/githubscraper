package com.main.service;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.main.dto.Passwordreset;
import com.main.dto.UserRequest;
import com.main.entity.User;
import com.main.repository.UserRepository;
import com.main.translator.UserTranslator;


@Service
public class UserService {
	
	
	@Autowired
	private UserTranslator translator;
	
	
	@Autowired
	private UserRepository repository;
	
	
	//reset password
	public String passwordreset(Passwordreset reset) {
		Optional<User> user = repository.findByusername(reset.getUsername());
		if(user.isPresent()) {
			User ur = user.get();
		if(!reset.getNewpassword().equals(reset.getConfirmpassword())) {
			return "password didnot match";
		}
		else {
			ur.setPassword(reset.getNewpassword());
			repository.save(ur);
			return " password reset sucessfully";
		}
	}
	else {
		return "user not found";
	}
 }
	
	//save the data
	public User save(UserRequest request) {
		return repository.save(translator.requestentity(request));
	}
	
	
	//login 
	public String login(UserRequest request) {
		Optional<User> user = repository.findByusername(request.getUsername());
	
		if(user.isPresent()) {
			User ur = user.get();
			if(ur.getPassword().equals(request.getPassword())) {
				return "sucessfully login";
			}
			else {
				return "login not sucessfully";
			}
		}
		else {
			return "user not found";
		}
		
		
	}

	
	
	
}
