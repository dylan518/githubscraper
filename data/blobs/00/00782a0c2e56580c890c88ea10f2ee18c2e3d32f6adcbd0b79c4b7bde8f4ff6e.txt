package com.te.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.te.model.User;
import com.te.service.UserService;

@Controller
public class FormController {

	@Autowired
	private UserService userService;

	@ModelAttribute // at method level we use for adding common data to the all the views
	public void commonDataForModel(Model model) {
		model.addAttribute("Header", "Welcome to SignUp page");
		model.addAttribute("desc", "we are using sign up page to set data ");

	}

	@RequestMapping("/form")
	public String form() {
		return "form";
	}

	// using @ModelAttribute-it will take all the values from form and set to the
	// user object
	// and it will automatically sets the values to the model object to pass from
	// controller to the view
	@RequestMapping(path = "/processForm", method = RequestMethod.POST)
	public String handleForm(@ModelAttribute User user, Model model) {
		System.out.println(user);
		int createUser = this.userService.createUser(user);
		model.addAttribute("msg", "User with Id "+createUser+" is Added Successfully!!!!!!");
		
		return "success";
	}

	/*
	 * //without using @ModelAttribute and using @Requestparam
	 * 
	 * @RequestMapping(path = "processForm",method =RequestMethod.POST) public
	 * String handleForm(
	 * 
	 * @RequestParam("email") String email,
	 * 
	 * @RequestParam("username") String name,
	 * 
	 * @RequestParam("password") String password,Model model) {
	 * 
	 * User user=new User(); user.setEmail(email); user.setUsername(name);
	 * user.setPassword(password);
	 * 
	 * System.out.println(user); model.addAttribute("user", user);
	 * 
	 * 
	 * return "success"; }
	 * 
	 */
}
