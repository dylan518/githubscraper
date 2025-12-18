package santiagotettamanti.com.doodleadoptions.shelter;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import santiagotettamanti.com.doodleadoptions.address.AddressController;
import santiagotettamanti.com.doodleadoptions.address.AddressService;

import java.util.List;

@RestController
public class ShelterController {
    private final ShelterService shelterService;

    @Autowired
    public ShelterController(ShelterService shelterService) {
        this.shelterService = shelterService;
    }

    @GetMapping ("/shelter")
    public List<Shelter> getAllShelters() {
        return shelterService.getAllShelters();
    }

    @GetMapping ("/shelter/{id}")
    public Shelter getShelterById(@RequestBody Shelter shelter, @PathVariable Integer id) {
        return shelterService.getShelterById(id);
    }

    @PostMapping ("/shelter")
    public Shelter createShelter(@RequestBody Shelter shelter) {
        return shelterService.createShelter(shelter);
    }

    @DeleteMapping ("/shelter/{id}")
    public Shelter deleteShelterById(@RequestBody Shelter shelter, @PathVariable Integer id) {
        return shelterService.deleteShelterById(id);
    }

}
