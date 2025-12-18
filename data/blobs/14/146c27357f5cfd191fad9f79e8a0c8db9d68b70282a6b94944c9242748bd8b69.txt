package com.ecommerce.auction.serviceImpl;



import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ecommerce.auction.entities.Admin;
import com.ecommerce.auction.repository.AdminRepos;
import com.ecommerce.auction.service.AdminService;


@Service

public class AdminServImpl implements AdminService {
	@Autowired
	public AdminRepos adminRepos;
	

	@Override
	public Admin saveAdmin(Admin admin) {
		
		return adminRepos.save(admin);
	}


	@Override
	public List<Admin> getalllistAdmin() {
		
		return adminRepos.findAll();
	}


	@Override
	public Admin getAdminByid(Long id) {
		
		return adminRepos.getById(id);
	}


	@Override
	public void deleteAdmin(Long Adminid) {
		
		
	}

}
