package com.ecomapi.serviceimpl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ecomapi.Repository.UserRepo;
import com.ecomapi.entities.User;
import com.ecomapi.service.UserService;

@Service
public class UserServiceImpl implements UserService{

	@Autowired UserRepo userRepo;
	
	@Override
	public boolean userRegister(User user){
		if(this.userRepo.save(user)!=null)
			return true;
	
		return false;
	}

	@Override
	public User userLogin(User user) {
		user=this.userRepo.findByEmailAndPassword(user.getEmail(),user.getPassword());
		return user;
	}

	@Override
	public List<User> getAllUsers() {
		return (List<User>) this.userRepo.findAll();
	}

	@Override
	public boolean deleteUser(int id) {
		this.userRepo.deleteById(id);
		return true;
	}

	@Override
	public User getUser(int userId) {
		User user=this.userRepo.findById(userId).get();
		if(user!=null)
			return user;
		return null;
	}

}
