package com.vickee.restapp.serviceimpl;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.vickee.restapp.model.MobileShop;
import com.vickee.restapp.repository.MobileShopRepo;
import com.vickee.restapp.service.MobileShopService;

@Service
public class MobileShopServiceImpl implements MobileShopService {

	
	
	MobileShopRepo repo;
	
	
	public MobileShopServiceImpl(MobileShopRepo repo) {
		super();
		this.repo = repo;
	}

	@Override
	public void addMobileShop(MobileShop shop) {
		repo.save(shop);
	}

	@Override
	public MobileShop getMobileShop(int mid) {
	    Optional<MobileShop> mobileOptional = repo.findById(mid);
	    return mobileOptional.orElse(null);
	}
	
	@Override
	public List<MobileShop> getAllMobileShop() {
		return repo.findAll();
	}

	@Override
	public void updateMobileShop(MobileShop shop) {
		repo.save(shop);
		
	}

	@Override
	public void deleteMobileShop(int mid) {
		repo.deleteById(mid);
		
	}

}
