package com.xworkz.forest.service;

import com.xworkz.forest.dto.ForestDto;
import com.xworkz.forest.repo.ForestRepo;
import com.xworkz.forest.repo.ForestrepoImpl;

public class ServiceImpl implements ForestService {
	ForestDto dto =new ForestDto();
	
	ForestRepo repo = new ForestrepoImpl();
	
	@Override
	public boolean save(ForestDto dto) {
		
		if(dto!= null) {
			if(dto.getId()>0) {
				if(dto.getName()!= null) {
					repo.saving(dto);
					return true;
				}
				System.out.println(" name is not valid");
				return false;
			}
			System.out.println("id is not valid");
			return false;
		}
		 System.out.println("dto is not valid");
		return false;
	}

	@Override
	public ForestDto Reading(int id) {
		System.out.println("Running read");
		if(id>0) {
			System.out.println("validated");
			return repo.Reading(id);
		}
		
		return null;
	}
	
	@Override
	public boolean FindByID(int id) {
		System.out.println("Running read");
		if(id>0) {
			System.out.println("validated");
			return repo.FindByID(id);
		}
		
		return false;
	}

	public  boolean UpdateByID(int id,String name) {
		 if(id>0 ) {
			 
			 System.out.println("validated");
			 return repo.UpdateByID(id, name);
			 
			 
		 }
		return  false;
	}

	@Override
	public boolean Delete(int id) {
		if(id>0 ) {
			 
			 System.out.println("validated");
			 return repo.Delete(id);
			 
			 
		 }
		return false;
	}

	

}
