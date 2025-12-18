package com.space.suppourting.controllers;


import com.space.suppourting.etity.Member;
import com.space.suppourting.etity.Student;
import com.space.suppourting.services.MemberService;
import com.space.suppourting.services.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class MemberConroler
{
    private MemberService memberService;
    @Autowired
    public MemberConroler(MemberService memberService) {
        this.memberService = memberService;
    }

    public MemberConroler() {

    }


    // HibernateMethod , returning model and view
    @GetMapping("/member")
    public String  listMember(Model model) {
        model.addAttribute("member", memberService.getAllMember());
        return "member";
    }


    @GetMapping("/member/new")
    public String createMember(Model model) {

        model.addAttribute("member", new Member());
        return "add-member";
    }


    @PostMapping("/member")
    public String saveStudent(@ModelAttribute("member") Member member ) {
        memberService.saveMember(member);
        return "redirect:/member";
    }

    @GetMapping("/member/edit/{id}")
    public String editStudent(@PathVariable Long id, Model model) {

        model.addAttribute("member", memberService.getmEMBERId(id));

        return "edit-member";

    }

    @PostMapping("/member/{id}")
    public String updateStudent(@PathVariable Long id ,@ModelAttribute("member") Member member, Model model) {


        Member editedMember = memberService.getmEMBERId(id);
        editedMember.setId(id);
        editedMember.setFirstName(member.getFirstName());
        editedMember.setStatus(member.getStatus());
        editedMember.setContact(member.getContact());




        memberService.updateMember(editedMember);

        return "redirect:/member";

    }

    @GetMapping("/member/{id}")
    public String deleteStudent(@PathVariable Long id, Model model) {

        Member member= memberService.deleteMember(id);

        return "redirect:/member";

    }

}
