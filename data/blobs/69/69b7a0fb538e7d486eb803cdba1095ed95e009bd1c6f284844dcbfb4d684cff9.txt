package com.example.demo;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@RestController
public class WalletController {

	@Autowired
	WalletRepository repo;
	
	@Autowired 
	WalletService service;
	
	@GetMapping(value="/showCustomerWallet/{id}")
	public List<Wallet> showCustomerWallet(@PathVariable int id) {
		return repo.findAll();
	}
	
	@GetMapping(value="/searchCustomerWalletInfo/{id}/{walType}")
	public Wallet showCustomerWalletInfo(@PathVariable int id, 
			@PathVariable String walType) {
		return service.showCustomerWalletInfo(id, walType);
	}
}
