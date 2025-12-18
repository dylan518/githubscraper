package com.limir.solidprincipals.single_responsibility.bad;

import java.util.ArrayList;
import java.util.List;

public class UserManager {
    private final List<User> users = new ArrayList<>();

    public void registerUser(String username, String password) {
        if (isValidUsername(username) && isValidPassword(password)) {
            users.add(new User(username, password));
            System.out.println("User " + username + " registered successfully");
        } else {
            System.out.println("Invalid username or password");
        }
    }

    private boolean isValidUsername(String username) {
        // Validation logic
        return  username != null && username.trim().isEmpty();
    }

    public boolean isValidPassword(String password) {
        // Validation logic
        return password != null && password.trim().isEmpty();
    }

    public List<User> getUsers() {
        return users;
    }
}

class User {
    String userName;
    String password;

    public User(String name, String password) {
        this.userName = name;
        this.password = password;
    }

    public String getName() {
        return userName;
    }

    public String getPassword() {
        return password;
    }
}