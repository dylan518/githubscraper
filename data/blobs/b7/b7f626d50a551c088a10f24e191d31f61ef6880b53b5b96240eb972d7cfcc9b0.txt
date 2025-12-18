package com.fabio.greatidea2.controllers;

import com.fabio.greatidea2.models.Idea;
import com.fabio.greatidea2.models.User;
import com.fabio.greatidea2.repositories.IdeaRepository;
import com.fabio.greatidea2.repositories.UserRepository;
import com.fabio.greatidea2.services.IdeaService;
import com.fabio.greatidea2.services.UserService;
import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class UserController {
    @Autowired
    private final UserService userService;
    @Autowired
    private final IdeaService ideaService;
    @Autowired
    private final UserRepository userRepository;
    @Autowired
    private final IdeaRepository ideaRepository;


    public UserController(UserService userService, IdeaService ideaService, UserRepository userRepository,
                          IdeaRepository ideaRepository) {
        this.userService = userService;
        this.ideaService = ideaService;
        this.userRepository = userRepository;
        this.ideaRepository = ideaRepository;
    }

    @GetMapping("/")
    public String home(@ModelAttribute("user") User user, @ModelAttribute("user_log") User user_log) {
        return "loginRegistration";
    }


    @RequestMapping(value = "/registration", method = RequestMethod.POST)
    public String registerUser(@Valid @ModelAttribute("user") User user, BindingResult result, HttpSession session) {
        if (result.hasErrors()) {
            return "loginRegistration";
        } else {
            User u = userService.registerUser(user);
            session.setAttribute("userId", u.getId());
            return "redirect:/ideas";
        }

    }


    @PostMapping(value = "/login")
    public String login(@ModelAttribute("user") User user, BindingResult result,
                        @RequestParam("email_log") String email, @RequestParam("password_log") String password, HttpSession session,
                        Model model) {
        if (userService.authenticateUser(email, password) == true) {
            User u = userService.findByEmail(email);
            session.setAttribute("userId", u.getId());
            return "redirect:/ideas";
        } else {
            model.addAttribute("error", "Invalid Credentials. Please try again.");
            return "loginRegistration";

        }
    }

    @RequestMapping("/ideas")
    public String home(Model model, HttpSession session) {
        List<Idea> ideas = ideaService.findAllIdeas();
        model.addAttribute("ideas", ideas);
        User u = userService.findUserById((Long) session.getAttribute("userId"));
        model.addAttribute("user", u);
        return "index";
    }

    @GetMapping("/ideas/new")
    public String createIdea(@ModelAttribute("idea") Idea idea) {
        return "newIdea";
    }

    @PostMapping("/ideas/new")
    public String createIdeaPost(@Valid @ModelAttribute("idea") Idea idea, BindingResult result, HttpSession session) {
        if (result.hasErrors()) {
            return "newIdea";
        } else {
            User u = userService.findUserById((Long) session.getAttribute("userId"));
            idea.setCreator(u);
            Idea m = ideaRepository.save(idea);
            return "redirect:/ideas";
        }
    }

    @GetMapping("/show/{id}")
    public String show(@PathVariable("id") Long id, Model model) {
        Idea m = ideaService.findIdeaById(id);
        model.addAttribute("idea", m);
        model.addAttribute("likers", userService.getAllLIkers(id));
        return "showIdea";
    }

    @GetMapping("/ideas/edit/{id}")
    public String edit(@PathVariable("id") Long id, Model model) {
        Idea m = ideaService.findIdeaById(id);
        model.addAttribute("idea", m);
        return "editIdea";
    }

    @PostMapping("/ideas/edit/{id}")
    public String actuallyEdit(@PathVariable("id") Long id, @Valid @ModelAttribute("idea") Idea idea,
                               BindingResult result) {
        if (result.hasErrors()) {
            return "editIdea";
        } else {
            Idea old = ideaService.findIdeaById(id);
            idea.setCreator(old.getCreator());
            idea.setLikers(old.getLikers());
            ideaRepository.save(idea);
            return "redirect:/ideas";
        }
    }

    @GetMapping("/like/{id}")
    public String like(@PathVariable("id") Long id, HttpSession session) {
        User u = userService.findUserById((Long) session.getAttribute("userId"));
        Idea m = ideaService.findIdeaById(id);
        m.getLikers().add(u);
        ideaRepository.save(m);
        return "redirect:/ideas";
    }

    @GetMapping("/unlike/{id}")
    public String unlike(@PathVariable("id") Long id, HttpSession session) {
        User u = userService.findUserById((Long) session.getAttribute("userId"));
        Idea m = ideaService.findIdeaById(id);
        for (int i = 0; i < m.getLikers().size(); i++) {
            if (u.getId() == m.getLikers().get(i).getId()) {
                m.getLikers().remove(i);
                break;
            }
        }
        ideaRepository.save(m);
        return "redirect:/ideas";
    }
 //  @GetMapping("/show/{id}")
  //  public String showLikes(@PathVariable("id")Long id,@ModelAttribute("usersLikes") User userLike, Model model){
  //      model.addAttribute("usersLikes",userService.findUserById(id));
   //    model.addAttribute("idea", ideaService.findIdeaById(id));
   //     return "showIdea";


  //  }


    @GetMapping("/delete/{id}")
    public String delete(@PathVariable("id") Long id) {
        ideaRepository.deleteById(id);
        return "redirect:/ideas";
    }

    @RequestMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/";
    }
}
