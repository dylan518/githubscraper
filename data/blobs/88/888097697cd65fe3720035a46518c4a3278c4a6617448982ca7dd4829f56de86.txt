package com.amar.hello_world.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CalculatorController {

	
	@GetMapping("/{op}")
	public String calculate(@PathVariable("op") String op, @RequestParam("value1") Integer value1, @RequestParam("value2") Integer value2) {
		
		String response = "";
		switch(op) {
		case "add":
				response = String.valueOf(value1 + value2);
			break;
		case "sub":
			response = String.valueOf(value1 - value2);
			break;
		case "mul":
			response = String.valueOf(value1 * value2);
			break;
		case "div":
			response = String.valueOf(value1 / value2);
			break;
		default:
			response = "Invalid Operation, Please provide one [add, sub, mul, div]";
			break;
		}
		return response;
	}
	
	@GetMapping("/hello")
	public String calculate() {
		
		return "Hello World!!";
	}
}
