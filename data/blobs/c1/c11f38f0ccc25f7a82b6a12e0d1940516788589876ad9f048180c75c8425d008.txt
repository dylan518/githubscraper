package tn.esprit.tp8_yassine_ferchichi.Controller;

import org.springframework.web.bind.annotation.*;
import tn.esprit.tp8_yassine_ferchichi.Service.IEquipeService;
import tn.esprit.tp8_yassine_ferchichi.entities.Equipe;

import java.util.List;
@RestController
@RequestMapping("/equipe")
public class EquipeRestController {
    IEquipeService iEquipeService;

    @GetMapping("/affichertout")
    public List<Equipe> retrieveAllEquipes() {

        return iEquipeService.retrieveAllEquipes();
    }
    @PostMapping("/ajout")
    public Equipe addEquipe(@RequestBody Equipe e){
        return iEquipeService.addEquipe(e);
    }
    @PutMapping("/modifierEquipe")
    public Equipe updateEquipe(@RequestBody Equipe f){

        return iEquipeService.updateEquipe(f);
    }
    @GetMapping("/afficherEquipe/{idEquipe}")
    public Equipe retrieveEquipe(@PathVariable("idEquipe") long idEquipe) {
        return iEquipeService.retrieveEquipe(idEquipe);
    }

    @DeleteMapping("/supprimerEquipe/{idEquipe}")
    public void removeEquipe(@PathVariable("idEquipe") long idEquipe) {

        iEquipeService.removeEquipe(idEquipe);
    }
}
