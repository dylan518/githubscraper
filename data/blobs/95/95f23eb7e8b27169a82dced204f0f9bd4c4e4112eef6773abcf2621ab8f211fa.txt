package hu.progmatic.person_expenses.controller;

import hu.progmatic.person_expenses.model.Person;
import hu.progmatic.person_expenses.service.PersonService;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.Date;

@Controller
@AllArgsConstructor
public class PersonController {
    private PersonService personService;

    @GetMapping("/persons")
    public String getAllPersons(Model model) {
        model.addAttribute("persons", personService.getAllPersons());
        return "person/persons";
    }
    @GetMapping("/addPerson")
    public String addNewPerson(Model model) {
        model.addAttribute("newPerson", new Person());
        return "person/addPerson";
    }
    @GetMapping("/modifyName")
    public String modifyName() {
        return "person/modifyName";
    }
    @PostMapping("/modifyName")
    public String modifyLastName(@RequestParam("id") Long id,
                                 @RequestParam("Name") String newName) {
        personService.modifyName(id, newName);
        return "redirect:/persons";
    }

    @GetMapping("/modifyBirthplace")
    public String modifyBirthplace() {
        return "person/modifyBirthplace";
    }
    @PostMapping("/ modifyBirthplace")
    public String modifyBirthplace(@RequestParam("id") Long id,
                                 @RequestParam("Birthplace") String newBirthplace) {
        personService.modifyBirthplace(id, newBirthplace);
        return "redirect:/persons";
    }
  /*  @GetMapping("/modifyBirthdate")
    public Date modifyBirthdate() {
        return "person/modifyBirthdate";   //???hogy kell, pirosozza
    }*/

    @GetMapping("/modifyEmail")
    public String modifyEmail() {
        return "person/modifyEmail";
    }
    @PostMapping("/modifyEmail")
    public String modifyEmail(@RequestParam("id") Long id,
                                 @RequestParam("Email") String newEmail) {
        personService.modifyEmail(id, newEmail);
        return "redirect:/persons";
    }
}
