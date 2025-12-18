package com.dh.proyect.DentalAppoiments.services.dto;


import lombok.Getter;
import lombok.Setter;
import org.springframework.stereotype.Component;

@Getter
@Setter
@Component
public class DentistDto {

    public Long id;
    public Integer registration;
    public String name;
    public String lastName;

    public DentistDto(Integer registration, String name, String lastName) {
        this.registration = registration;
        this.name = name;
        this.lastName = lastName;
    }
}




