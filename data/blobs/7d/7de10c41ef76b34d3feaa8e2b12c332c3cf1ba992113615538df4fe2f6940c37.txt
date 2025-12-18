package co.develhope.h2mock.entities;

import lombok.Data;

import javax.persistence.*;

@Entity
@Table
@Data
public class Student {

        private String lastName;
        private String firstName;

        @Id
        @GeneratedValue(strategy = GenerationType.AUTO)
        private long studentId;

        @Column(unique=true)
        private String email;

}


