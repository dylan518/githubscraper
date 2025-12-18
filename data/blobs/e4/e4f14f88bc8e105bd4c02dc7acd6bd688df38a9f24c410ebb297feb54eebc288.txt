package com.example.seekhelp.entities;

import lombok.*;

import javax.persistence.*;
import java.io.Serializable;
import java.util.List;


@Getter
@Setter
@Entity
public class User implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY, generator = "JDBC")
    private Integer userId;
    private String email;
    private String password;
    private String name;
    private String city;
    private String phone;
    private int isConsultant;
    private String createdAt;

    @OneToMany(mappedBy = "owner")
    private List<Post> posts;

    @OneToMany(mappedBy = "user")
    private List<Match> matches;

    @OneToOne(mappedBy = "user")
    private Skill skill;
}