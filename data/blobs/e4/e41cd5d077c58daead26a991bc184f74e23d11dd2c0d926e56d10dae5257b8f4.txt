package com.example.dto;

import com.example.model.facility.FacilityType;
import com.example.model.facility.RentType;
import org.springframework.validation.Errors;
import org.springframework.validation.Validator;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Pattern;

public class FacilityDto implements Validator {

    private Integer facilityId;

    @NotBlank(message = "Tên dịch vụ không được để trống.")
    @Pattern(regexp = "^(([\\p{Lu}][\\p{Ll}]{1,8})(\\s([\\p{Lu}]|[\\p{Lu}][\\p{Ll}]{1,10})){0,5}( \\d*)?)| *$",
            message = "Tên dịch vụ được phép chứa số, và các kí tự đầu tiên của mỗi từ phải viết hoa.")
    private String facilityName;

    @NotBlank(message = "Diện tích sử dụng không được để trống.")
    @Pattern(regexp = "^[1-9]\\d*| *$", message = "Diện tích sử dụng phải là số nguyên dương.")
    private String facilityArea;

    @NotBlank(message = "Chi phí thuê không được để trống.")
    @Pattern(regexp = "^[1-9]\\d*| *$", message = "Chi phí thuê (VNĐ) phải là số nguyên dương.")
    private String facilityCost;

    @NotBlank(message = "Số người tối đa không được để trống.")
    @Pattern(regexp = "^[1-9]\\d*| *$", message = "Số người tối đa phải là số nguyên dương.")
    private String facilityMaxPeople;
    
    private String facilityStandardRoom;
    private String facilityDescriptionOtherConvenience;

    @Pattern(regexp = "^[1-9]\\d*| *$", message = "Diện tích hồ bơi phải là số nguyên dương.")
    private String facilityPoolArea;

    @Pattern(regexp = "^[1-9]\\d*| *$", message = "Số tầng phải là số nguyên dương.")
    private String facilityNumberOfFloors;
    private String facilityFree;
    private FacilityType facilityType;
    private RentType rentType;

    public FacilityDto() {
    }

    public FacilityDto(Integer facilityId, String facilityName, String facilityArea, String facilityCost, String facilityMaxPeople,
                       String facilityStandardRoom, String facilityDescriptionOtherConvenience, String facilityPoolArea,
                       String facilityNumberOfFloors, String facilityFree, boolean isDelete, FacilityType facilityType,
                       RentType rentType) {
        this.facilityId = facilityId;
        this.facilityName = facilityName;
        this.facilityArea = facilityArea;
        this.facilityCost = facilityCost;
        this.facilityMaxPeople = facilityMaxPeople;
        this.facilityStandardRoom = facilityStandardRoom;
        this.facilityDescriptionOtherConvenience = facilityDescriptionOtherConvenience;
        this.facilityPoolArea = facilityPoolArea;
        this.facilityNumberOfFloors = facilityNumberOfFloors;
        this.facilityFree = facilityFree;
        this.facilityType = facilityType;
        this.rentType = rentType;
    }

    public Integer getFacilityId() {
        return facilityId;
    }

    public void setFacilityId(Integer facilityId) {
        this.facilityId = facilityId;
    }

    public String getFacilityName() {
        return facilityName;
    }

    public void setFacilityName(String facilityName) {
        this.facilityName = facilityName;
    }

    public String getFacilityArea() {
        return facilityArea;
    }

    public void setFacilityArea(String facilityArea) {
        this.facilityArea = facilityArea;
    }

    public String getFacilityCost() {
        return facilityCost;
    }

    public void setFacilityCost(String facilityCost) {
        this.facilityCost = facilityCost;
    }

    public String getFacilityMaxPeople() {
        return facilityMaxPeople;
    }

    public void setFacilityMaxPeople(String facilityMaxPeople) {
        this.facilityMaxPeople = facilityMaxPeople;
    }

    public String getFacilityStandardRoom() {
        return facilityStandardRoom;
    }

    public void setFacilityStandardRoom(String facilityStandardRoom) {
        this.facilityStandardRoom = facilityStandardRoom;
    }

    public String getFacilityDescriptionOtherConvenience() {
        return facilityDescriptionOtherConvenience;
    }

    public void setFacilityDescriptionOtherConvenience(String facilityDescriptionOtherConvenience) {
        this.facilityDescriptionOtherConvenience = facilityDescriptionOtherConvenience;
    }

    public String getFacilityPoolArea() {
        return facilityPoolArea;
    }

    public void setFacilityPoolArea(String facilityPoolArea) {
        this.facilityPoolArea = facilityPoolArea;
    }

    public String getFacilityNumberOfFloors() {
        return facilityNumberOfFloors;
    }

    public void setFacilityNumberOfFloors(String facilityNumberOfFloors) {
        this.facilityNumberOfFloors = facilityNumberOfFloors;
    }

    public String getFacilityFree() {
        return facilityFree;
    }

    public void setFacilityFree(String facilityFree) {
        this.facilityFree = facilityFree;
    }

    public FacilityType getFacilityType() {
        return facilityType;
    }

    public void setFacilityType(FacilityType facilityType) {
        this.facilityType = facilityType;
    }

    public RentType getRentType() {
        return rentType;
    }

    public void setRentType(RentType rentType) {
        this.rentType = rentType;
    }

    @Override
    public boolean supports(Class<?> clazz) {
        return false;
    }

    @Override
    public void validate(Object target, Errors errors) {

    }
}
