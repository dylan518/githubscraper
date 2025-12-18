package com.first.demo.service.impl;

import com.first.demo.mapper.EmpMapper;
import com.first.demo.pojo.Emp;
import com.first.demo.service.EmpService;
import org.apache.ibatis.annotations.Select;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class EmpServiceImpl implements EmpService {

    @Autowired
    private EmpMapper empMapper;

    @Override
    public Emp login(Emp emp) {
        return empMapper.getUsernameAndPassword(emp);
    }

    @Override
    public void add(Emp emp) {
        // 设置默认值
        emp.setPassword("123456");
        emp.setCreateTime(LocalDateTime.now());
        emp.setUpdateTime(LocalDateTime.now());
        empMapper.add(emp);
    }
}
