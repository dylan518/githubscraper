package com.pranitproject.controller;

import java.util.List;

import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.pranitproject.entity.Candidate;
import com.pranitproject.entity.IndianUser;
import com.pranitproject.service.UserServiceInterface;

@RestController
@CrossOrigin(origins = "*")
public class UserController {

	@Autowired
	private UserServiceInterface fs;

	@PostMapping("/registeruser/add")
	public IndianUser register(@RequestBody IndianUser IndianUser) {
		return fs.createProfile(IndianUser);
	}

	@DeleteMapping("/delete/{userName}")
	public String deleteProfile(@PathVariable("userName") String uName) {

		fs.deleteProfile(uName);

		return "profile deleted " + uName;
	}

	@GetMapping("/login/{ui}/{pass}")
	public IndianUser loginUser(@PathVariable("ui") String userName, @PathVariable("pass") String password) {
		IndianUser f = fs.loginUserService(userName, password);
		return f;
	}

	@GetMapping("/user/viewall")
	public List<IndianUser> viewAllProfile() {
		List<IndianUser> ff = (List<IndianUser>) fs.getAll();
		return ff;
	}

	@GetMapping("/candidate/viewallcandidate")
	public List<Candidate> viewAllCandidate() {
		List<Candidate> cList = (List<Candidate>) fs.getAllCandidate();
		return cList;
	}

	@Transactional
	@PutMapping("/user/vote/{uName}/{cName}")
	public Boolean votingmethod(@PathVariable("uName") String userName, @PathVariable("cName") String cName) {
		return fs.voting(userName, cName);

	}

	@GetMapping("/candidate/totalvote/{cname}")
	public int totalVote(@PathVariable("cname") String cName) {
		return fs.totalcountcandidate(cName);
	}
}
