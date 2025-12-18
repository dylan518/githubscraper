package enspy.mboumela.statsservice.controllers;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import enspy.mboumela.statsservice.dtos.conducteur.ConducteurDto1;
import enspy.mboumela.statsservice.dtos.conducteur.ConducteurDto2;
import enspy.mboumela.statsservice.dtos.conducteur.ConducteurDto3;
import enspy.mboumela.statsservice.dtos.conducteur.ConducteurJournalDto;
import enspy.mboumela.statsservice.services.ConducteurService;
import io.swagger.v3.oas.annotations.Operation;
import lombok.RequiredArgsConstructor;

@RestController
@RequiredArgsConstructor
public class ConducteurController {
	private final ConducteurService conducteurService;
	
	@Operation(summary = "renvoyer le nombre dde voyages")
    @GetMapping("/get-conducteur-data1")
    public ResponseEntity<List<ConducteurDto1>> data1() {
		List<ConducteurDto1> conducteurDto1 = conducteurService.calculNbrVoyageEffectue();
    	return new ResponseEntity<>(conducteurDto1, HttpStatus.OK);
    }
    
	@Operation(summary = "renvoyer le nombre d'avis")
    @GetMapping("/get-conducteur-data2")
    public ResponseEntity<List<ConducteurDto2>> data2() {
		List<ConducteurDto2> conducteurDto2 = conducteurService.calculAvis();
    	return new ResponseEntity<>(conducteurDto2, HttpStatus.OK);
    }
    
	@Operation(summary = "renvoyer le nombre de km parcourus")
    @GetMapping("/get-conducteur-data3")
    public ResponseEntity<List<ConducteurDto3>> data3() {
		List<ConducteurDto3> conducteurDto3 = conducteurService.calculNbrKm();
    	return new ResponseEntity<>(conducteurDto3, HttpStatus.OK);
    }
    
	@Operation(summary = "renvoyer le journal")
	@GetMapping("/get-conducteur-journal")
	public ResponseEntity<List<ConducteurJournalDto>> journal() {
		List<ConducteurJournalDto> list = conducteurService.calculJournal();
		return new ResponseEntity<>(list, HttpStatus.OK);
	}
}
