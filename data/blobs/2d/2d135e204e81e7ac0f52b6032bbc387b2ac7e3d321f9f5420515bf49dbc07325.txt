package org.example.TestingSystem_Assigment_4;

import javax.swing.text.Position;
import java.time.LocalDateTime;

public class Account {
    int id;
    String email;
    String username;
    String fullname;
    Department department;
    Position position;
    LocalDateTime createDate;
    Group[] groups;
    public Account(){}
    public Account(int id,String email, String username, String FirstName,String LastName)
    {
        this.id = id;
        this.email = email;
        this.username = username;
        this.fullname = FirstName + LastName;
    }
    public Account(int id, String email, String username, String FirstName, String LastName, Position position)
    {
        this.id = id;
        this.email = email;
        this.username = username;
        this.fullname = FirstName + LastName;
        this.position = position;
        this.createDate = LocalDateTime.now();
    }

    public Account(String username) {
        this.email = null;
        this.username = null;
        this.fullname = null;
        this.position = null;
        this.createDate = null;
    }
}
