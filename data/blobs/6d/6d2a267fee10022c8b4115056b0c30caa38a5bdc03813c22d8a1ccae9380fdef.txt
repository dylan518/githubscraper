package com.knoldus.employeemanagementsystem.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "address")
public class Address {

    @Id
    @SequenceGenerator(name = "address_sequence",
            sequenceName = "address_sequence",
            allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.SEQUENCE,
            generator = "address_sequence")
    @Column(name = "id", nullable = false)
    private Long id;

    @NotEmpty(message = "HouseNo can't be empty")
    private Long houseNo;

    @NotEmpty(message = "city can't be empty")
    @Size(min = 2, message = "city should have at least 2 characters")
    private  String city;

    @NotEmpty(message = "State can't be empty")
    @Size(min = 2, message = "State should have at least 2 characters")
    private String state;


}
