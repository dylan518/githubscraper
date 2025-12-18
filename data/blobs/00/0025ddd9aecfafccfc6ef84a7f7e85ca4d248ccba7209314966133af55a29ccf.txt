package org.example.ms_utilisateur.service;

import org.example.ms_utilisateur.entity.User;
import org.example.ms_utilisateur.repository.IUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {

    @Autowired private IUserRepository userRepository;

    public List<User> getAll() {
        return userRepository.findAll();
    }

    public User createUser(User user) {
        return userRepository.save(user);
    }

    public void deleteUser(long id) {
        userRepository.deleteById(id);
    }

    public User updateUser(long id, User user) {
        User returnedUser = userRepository.findById(id).orElseThrow();
        returnedUser.setName(user.getName());
        returnedUser.setEmail(user.getEmail());
        userRepository.save(returnedUser);
        return returnedUser;
    }

    public User getById(long id) {
        return userRepository.findById(id).orElseThrow();
    }
}
