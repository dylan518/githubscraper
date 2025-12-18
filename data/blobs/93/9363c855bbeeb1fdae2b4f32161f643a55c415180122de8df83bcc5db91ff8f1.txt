package com.abdelrahman.spring_boot_example.student;

import com.abdelrahman.spring_boot_example.course.Course;
import com.abdelrahman.spring_boot_example.major.Major;
import com.abdelrahman.spring_boot_example.project.Project;
import jakarta.persistence.*;
import lombok.Data;
import java.util.Date;

@Data
@Entity
@Table(name = "student")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "name", length = 100)
    private String name;

    @Column(name = "email", length = 100)
    private String email;

    @Column(name = "phone_number")
    private int phoneNumber;

    @Column(name = "date_of_birth")
    @Temporal(TemporalType.DATE)
    private Date dateOfBirth;

    @Column(name = "address", length = 255)
    private String address;

    @Column(name = "major_id")
    private int majorId;

    @Column(name = "course_id")
    private int courseId;

    @Column(name = "project_id")
    private int projectId;

    @Column(name = "created_at")
    @Temporal(TemporalType.TIMESTAMP)
    private Date createdAt;

    @Column(name = "updated_at")
    @Temporal(TemporalType.TIMESTAMP)
    private Date updatedAt;
}
