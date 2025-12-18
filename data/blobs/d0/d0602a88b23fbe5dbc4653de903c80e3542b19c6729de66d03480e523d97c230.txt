package in.ashokit.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import in.ashokit.binding.contact;
import in.ashokit.repository.ContactRepostory;

@Service
public class contactServiceIMPL implements contactService{

	@Autowired
	private ContactRepostory repo;

	@Override
	public String upsert(contact Contact) {
		repo.save(Contact);
		return "succes";
	}

	@Override
	public List<contact> getAllcontact() {
		return repo.findAll();
		 
	}

	@Override
	public contact getId(int cid) {
		Optional<contact> id = repo.findById(cid);
		if(id.isPresent()) {
			return id.get();
		}
		return null;
	}

	@Override
	public String deleteId(int cid) {
		repo.deleteById(cid);
		return "success";
	}
	 

}
