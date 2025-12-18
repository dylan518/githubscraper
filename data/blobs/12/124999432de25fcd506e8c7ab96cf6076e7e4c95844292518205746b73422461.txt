package com.fooddifferently.fd.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import java.util.List;

/**
 * Data Transfer Object (DTO) representing restaurant information.
 */
public class RestaurantDTO {

    @JsonProperty("id")
    @NotBlank(message = "ID cannot be blank")
    private Long id;

    @JsonProperty("name")
    @NotBlank(message = "Name cannot be blank")
    private String name;

    @JsonProperty("address")
    @NotBlank(message = "Address cannot be blank")
    private String address;

    @JsonProperty("phoneNumber")
    @NotBlank(message = "Phone number cannot be blank")
    private String phoneNumber;

    @JsonProperty("rating")
    private Double rating;

    @JsonProperty("photoUrls")
    private List<String> photoUrls;

    /**
     * Default constructor for RestaurantDTO.
     */
    public RestaurantDTO() {

    }


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public Double getRating() {
        return rating;
    }

    public void setRating(Double rating) {
        this.rating = rating;
    }

    public List<String> getPhotoUrls() {
        return photoUrls;
    }

    public void setPhotoUrls(List<String> photoUrls) {
        this.photoUrls = photoUrls;
    }
}
