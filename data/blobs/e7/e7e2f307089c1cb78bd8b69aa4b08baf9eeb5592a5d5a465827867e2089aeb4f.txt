package com.ecotech.usmt.services.impl;


import com.ecotech.usmt.models.User;
import com.ecotech.usmt.exception.ResourceNotFoundException;
import com.ecotech.usmt.repositories.UserRepositry;
import com.ecotech.usmt.services.UserService;
import org.modelmapper.ModelMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ecotech.usmt.entities.UserDetails;
import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements UserService {
       @Autowired
       private UserRepositry userRepositry;
    @Autowired
    private ModelMapper modelMapper;

    @Override
    public User saveUser(User user) {
        UserDetails userDetails=  modelMapper.map(user,UserDetails.class);
        UserDetails userDetail=  userRepositry.save(userDetails);
       return modelMapper.map(userDetail,User.class);
    }

    @Override
    public List<User> getAllUser() {
        return userRepositry.findAll().stream().map(userDetails -> modelMapper.map(userDetails,User.class)).collect(Collectors.toList());
    }

    @Override
    public User getUser(long userid) {
        return userRepositry.findById(userid).map(userDetails -> modelMapper.map(userDetails,User.class)).orElseThrow(()->new ResourceNotFoundException("user is not found "+userid));
    }
    public User loginByEmailAndPassword(String email,String Password) {
        return userRepositry.findByEmailAndPassword(email,Password).map(userDetails -> modelMapper.map(userDetails,User.class)).orElseThrow(()->new ResourceNotFoundException("email or password not match "+email));
    }
}
