package com.service.impl;

import com.dao.ILoginDao;
import com.pojo.BookUser;
import com.service.IUserService;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import javax.annotation.Resource;
@Transactional
@Service("userService")
public class UserServiceImpl implements IUserService {
    @Resource
    private ILoginDao dao;
    @Override
    public BookUser login(String name, String password) {
        return dao.login(name,password);
    }

    public static void main(String[] args) {
        UserServiceImpl i = new UserServiceImpl();
        i.login("aaa","123");
    }
}
