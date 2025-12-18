package tourismpk.tourismpk.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import tourismpk.tourismpk.domain.Facilities;
import tourismpk.tourismpk.repository.FacilitiesRepo;

import java.util.List;
import java.util.Optional;

@Service
public class FacilitiesServiceImpl {

    @Autowired
    private FacilitiesRepo facilitiesRepo;

    public List<Facilities> getAllFacilities() {
        return facilitiesRepo.findAll();
    }

    public Optional<Facilities> getFacilitiesById (Integer id) {
        return facilitiesRepo.findById(id);
    }

    public Facilities saveFacilities (Facilities facilities) {
        return facilitiesRepo.save(facilities);

        }
    }
