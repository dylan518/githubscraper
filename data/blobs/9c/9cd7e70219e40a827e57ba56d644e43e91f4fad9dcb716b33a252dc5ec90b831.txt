package com.example.sisgestaskbe.repository;

import java.util.List;

import org.springframework.stereotype.Repository;

import com.example.sisgestaskbe.model.User;
import com.example.sisgestaskbe.model.mock.UserMock;

@Repository
public class UserRepository {

    public List<User> getAllUsersByRole() {
        UserMock userMock = new UserMock();
        return userMock.getAllUsersByRole();
    }

    public User newUser(User newUser) {
        UserMock userMock = new UserMock();
        return userMock.newUser();
    }
}
