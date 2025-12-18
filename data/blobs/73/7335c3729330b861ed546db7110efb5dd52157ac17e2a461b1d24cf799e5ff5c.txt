package com.demo.controller;


import com.demo.pojo.Emp;
import com.demo.pojo.Result;
import com.demo.service.EmpService;
import com.demo.utils.JwtUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@Slf4j
@RestController
@RequestMapping("/login")
public class LoginController {

    @Autowired
    private EmpService empService;

    /**
     * 登录检验
     *
     * @param emp
     * @return
     */
    @PostMapping
    public Result Login(@RequestBody Emp emp) {
        log.info("接受的用户名和密码是{}", emp);
        Emp emp1 = empService.login(emp);

        //登录成功，下发JWT令牌
        if (emp1 != null) {
            Map<String, Object> claims = new HashMap<>();
            claims.put("id", emp1.getId());
            claims.put("name", emp1.getName());
            claims.put("username", emp1.getUsername());

            String jwt = JwtUtils.generateJwt(claims);
            return Result.success(jwt);

        }

        //登录失败，返回错误信息
        return Result.error("用户名或密码错误");
    }

}
