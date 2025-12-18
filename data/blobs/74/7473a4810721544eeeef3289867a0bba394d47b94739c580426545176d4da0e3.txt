package com.app.dto;

import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.validation.constraints.NotBlank;

import com.app.Enum.Role;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonProperty.Access;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class DoctorSignup extends BaseSignup {

    @NotBlank(message = "Qualification required")
    private String qualification; // Doctor's qualification

    @NotBlank(message = "Availability required")
    private String availability; // Doctor's availability

    @Enumerated(EnumType.STRING)
    @JsonProperty(access = Access.READ_ONLY)
    private Role role = Role.DOCTOR; // Set the role to DOCTOR by default

    // Optionally include doctorId in case it's needed in response
    @JsonProperty(access = Access.READ_ONLY)
    private Long doctorId;

    // Constructor with fields
    public DoctorSignup(String firstname,String lastname, String email, String password, String contactNumber, String qualification, String availability) {
        super(firstname,lastname, email, password, contactNumber); // Call the constructor of BaseSignup
        this.qualification = qualification;
        this.availability = availability;
    }
}
