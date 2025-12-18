package org.equipmentmanager.model;

import lombok.*;


@Data
@AllArgsConstructor
@NoArgsConstructor
public class Office {
    String address;
    String department;

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
}
