package com.ureca.board.service;

import com.ureca.board.dao.UserDAO;
import com.ureca.board.dto.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    private UserDAO userDAO;

    @Override
    public void registerUser(User user) {
        userDAO.insertUser(user);
    }

    @Override
    public User findUserByUsername(String username) {
        return userDAO.getUserByUsername(username);
    }
}
