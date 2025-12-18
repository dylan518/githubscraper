package com.ticket.myticket.service.impl;

import java.time.Instant;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
//import org.springframework.security.core.userdetails.UserDetails;
//import org.springframework.security.core.userdetails.UserDetailsService;
//import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.yaml.snakeyaml.external.biz.base64Coder.Base64Coder;

import com.ticket.myticket.Exception.TicketException;
import com.ticket.myticket.Util.JWTUtil;
import com.ticket.myticket.dto.LoginRequestDTO;
import com.ticket.myticket.dto.LoginResponseDTO;
import com.ticket.myticket.dto.UserRequestDTO;
import com.ticket.myticket.model.User;
import com.ticket.myticket.repo.UserRepository;
import com.ticket.myticket.service.UserService;

@Service
public class UserServiceImpl implements UserService {

	
	@Autowired
	UserRepository urepo;
	
	@Autowired
	JWTUtil jwtUtil;

	@Override
	public String createUser(UserRequestDTO userRequestDTO) {

		if(!userRequestDTO.getPassword().equals(userRequestDTO.getConfirmPassword())) {
			throw new TicketException(HttpStatus.BAD_REQUEST, "Password and ConfirmPassword should be same", null);
		}
		User userSaved = urepo.save(this.convertUserRequestDTOToUser(userRequestDTO));
		return "User with email "+ userSaved.getEmail()+" saved successfully";
	}
	
	@Override
	public LoginResponseDTO login(LoginRequestDTO loginRequestDTO) {
		Optional<User> optUser = urepo.findByEmail(loginRequestDTO.getEmail());
		if(optUser.isPresent()) {
			String token = jwtUtil.createToken(optUser.get());
			return new LoginResponseDTO(token,token,new Date().getTime() + (30*60*1000));
		}
		throw new TicketException(HttpStatus.UNAUTHORIZED, "invalid username", null);	
	}
	
	
	public User convertUserRequestDTOToUser(UserRequestDTO userRequestDTO) {
		User user = new User();
		user.setName(userRequestDTO.getName());
		user.setEmail(userRequestDTO.getEmail());
		user.setDepartment(userRequestDTO.getDepartment());
		user.setPassword(userRequestDTO.getPassword());
		user.setRoles(new HashSet<>());
		user.setPassword(Base64Coder.encodeString(userRequestDTO.getPassword()));
		return user;
		
	}
	
	
//	@Override
//	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
//		Optional<User> opt = urepo.findByUserName(username);
//		if(opt.isEmpty()) {
//			throw new TicketException(HttpStatus.BAD_REQUEST, "UserName not found", null);
//		}
//		else {
//			User user = opt.get();
//			return new org.springframework.security.core.userdetails.User(username, user.getPassword(), null);
//		}
//	}
	
}
