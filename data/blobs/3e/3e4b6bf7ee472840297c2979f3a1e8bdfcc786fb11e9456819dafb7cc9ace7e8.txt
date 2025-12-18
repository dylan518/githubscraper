package com.demo.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.demo.entity.House;
import com.demo.entity.User;
import com.demo.mapper.HouseMapper;
import com.demo.mapper.UserMapper;
import com.demo.service.HouseService;
import jakarta.annotation.Resource;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class HouseServiceImpl extends ServiceImpl<HouseMapper, House> implements HouseService {
    @Resource
    private HouseMapper houseMapper;
    @Override
    public List<House> listAll()
    {
        return houseMapper.listAll();
    }
}
