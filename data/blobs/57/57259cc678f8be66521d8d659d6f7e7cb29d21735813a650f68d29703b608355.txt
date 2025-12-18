package com.upchiapas.javaparajuniors.models;
import static com.upchiapas.javaparajuniors.controllers.LoginController.users;
public  class ValidateUser {

    public void ingresarUsuario(String username, String password)
    {
        users.add(new User(username,password));
    }

    public boolean autenticarUser(String username, String password)
    {
        boolean status = false;
        User user = findUser(username);
        if(user != null && user.getPassword().equals(password))
        {
            status = true;
        }
        return status;
    }

    private User findUser(String username)
    {
        User user = null;
        boolean status = false;
        int index = 0;
        while (!status && index<users.size())
        {
            if(users.get(index).getUsername().equals(username))
            {
                user = users.get(index);
                status = true;
            }
            index++;
        }
        return user;
    }
}