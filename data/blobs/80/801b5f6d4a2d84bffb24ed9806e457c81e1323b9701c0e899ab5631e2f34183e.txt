package com.project.swp.entity;
import jakarta.persistence.*;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "Staff")
public class Staff {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "EmpID")
    private int empId;

    @Column(name = "UserName")
    private String userName;

    @Column(name = "Password")
    private String password;

    @Column(name = "EmpName")
    private String empName;

    @Column(name = "PhoneNumber")
    private String phoneNumber;

    @Column(name = "Email")
    private String email;

    @Column(name = "Picture")
    private String picture;

    @Column(name = "Status")
    private String status;

    @Column(name = "Salary")
    private Double salary;

    @Column(name = "TimeWork")
    private String timeWork;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumns({
            @JoinColumn(name = "RoleID", referencedColumnName="RoleID"),
            @JoinColumn(name = "ResID", referencedColumnName="ResID")
    })
    private Role role;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "CompanyID")
    private Company company;

}
