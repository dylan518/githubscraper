package com.ty.mobile_sim.controller;

import java.util.ArrayList;
import java.util.List;

import com.ty.mobile_sim.dao.Dao;
import com.ty.mobile_sim.dto.Mobile;
import com.ty.mobile_sim.dto.Sim;

public class SaveMobile {
	
	public static void main(String[] args) {
		Mobile mobile = new Mobile();
		List<Sim> sims = new ArrayList<Sim>();
		int[] id = {1,2};
		String[] provider = {"airter","bsnl"};
		String[] imrc = {"1232erw","juou898"};
		
		for(int i=0; i<id.length; i++) {
			Sim sim = new Sim();
			sim.setId(id[i]);
			sim.setProvider(provider[i]);
			sim.setImrc(imrc[i]);
			sims.add(sim);
		}
		
		mobile.setSims(sims);
		mobile.setCost(2000);
		mobile.setId(1);
		mobile.setName("samsung");
		
		Dao dao = new Dao();
		dao.saveMobile(mobile);
		System.out.println("saved the data");
	}

}
