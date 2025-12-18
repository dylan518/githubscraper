package com.ticketsystem.service;

import java.util.List;
import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import com.ticketsystem.entity.User;
import com.ticketsystem.entity.UserList;

@Service
public class UserServiceImpl implements UserService {

	@Autowired
	private RestTemplate restTemplate;

	String baseURL = "http://localhost:8094/";

	@Override
	public User addUser(User user) {
		restTemplate.postForEntity(baseURL + "addUser", user, User.class);
		return user;
	}

	@Override
	public int deleteUser(String username) {
		if (restTemplate.getForObject(baseURL + "user/" + username, User.class) != null) {
			restTemplate.delete(baseURL + "deleteUser/" + username);
			return 1;
		}

		else
			return 0;
	}

	@Override
	public User updatePassword(String username, String password) {
		restTemplate.put(baseURL + "updateUser/" + username + "/" + password, password, User.class);
		User updatedUser = restTemplate.getForObject(baseURL + "user/" + username, User.class);
		return updatedUser;
	}

	@Override
	public List<User> getAllUsers() {
		UserList userList = restTemplate.getForObject(baseURL + "users", UserList.class);
		List<User> users = userList.getUserList();
		return users;
	}

	@Override
	public User getUser(String username) {
		User user = restTemplate.getForObject(baseURL + "user/" + username, User.class);
		return user;
	}

//	@Override
//	public User getUserByUsernameAndPassword(User user) {
//		restTemplate.postForObject(baseURL+"login", user, User.class);
//		return user;
//		}
	@Override
	public User getUserByUsernameAndPassword(User user) {
		User responseUser = restTemplate.postForObject(baseURL + "login", user, User.class);
		return responseUser;
	}

}
