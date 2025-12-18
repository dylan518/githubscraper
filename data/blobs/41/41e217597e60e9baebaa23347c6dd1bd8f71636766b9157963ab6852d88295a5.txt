package com.example.sql_filter.controller;

import com.example.sql_filter.model.bo.SqlBO;
import com.example.sql_filter.model.vo.SqlVO;
import com.example.sql_filter.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
@RestController
@RequestMapping("hello")
public class HelloController {

    @Autowired
    private StudentService studentService;

    @PostMapping("good")
    public Object sql(@RequestBody List<SqlBO> sqlBO) {
        for (SqlVO sqlVO :studentService.queryList(sqlBO)) {
            System.out.println(sqlVO);
        }
        Map<String, Object> map = new HashMap<>();
        map.put("data", studentService.queryList(sqlBO));
        return map;
    }
}
