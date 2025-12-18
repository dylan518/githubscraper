package com.example.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.entities.Lead;
import com.example.repositories.LeadRepositoty;
@Service
public class LeadServiceImpl implements LeadService {
	
	@Autowired
	private LeadRepositoty leadRepo;

	@Override
	public void saveLeadInfo(Lead lead) {
		leadRepo.save(lead);
	}

	@Override
	public List<Lead> getAllLeads() {
		List<Lead> leads = leadRepo.findAll();
		return leads;
	}

	@Override
	public Lead findLeadById(long id) {
		Optional<Lead> findById = leadRepo.findById(id);
		Lead lead = findById.get();
		return lead;
	}

	@Override
	public void deleteById(long id) {
		leadRepo.deleteById(id);
	}

}
