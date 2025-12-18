package com.example.likelionnfirst.post.Controller;


import com.example.likelionnfirst.post.dto.MemberDto;
import com.example.likelionnfirst.post.service.MemberService;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
@AllArgsConstructor
public class MemberController {

    private MemberService memberService;

    @GetMapping("user/signup")
    public String signUpForm(){

        return "users/signup.html";
    }

    @PostMapping("user/signup")
    public String signup(MemberDto memberDto) {
        memberService.joinUser(memberDto);
        return "redirect:/";
    }

    @GetMapping("user/login")
    public String member() {
        return "users/login.html";
    }

    @GetMapping("user/admin")
    public String admin(Model model) {
        List<MemberDto> memberDtoList = memberService.getMemberList();
        model.addAttribute("memberList", memberDtoList);
        return "users/admin.html";

    }



}
