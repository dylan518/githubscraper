package com.funeralservice.pojo;

import javax.xml.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "employeesInOrder", propOrder = {
        "employeeInOrder"
})
public class EmployeesInOrder {

    @XmlElement(name = "employeeInOrder")
    private List<EmployeeInOrder> employeeInOrder = new ArrayList<>();

    public EmployeesInOrder() {
    }

    public EmployeesInOrder(List<EmployeeInOrder> employeesInOrder) {
        this.employeeInOrder = employeesInOrder;
    }

    public List<EmployeeInOrder> getEmployeeInOrder() {
        return employeeInOrder;
    }

    public void setEmployeeInOrder(List<EmployeeInOrder> employeeInOrder) {
        this.employeeInOrder = employeeInOrder;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        EmployeesInOrder that = (EmployeesInOrder) o;
        return Objects.equals(employeeInOrder, that.employeeInOrder);
    }

    @Override
    public int hashCode() {
        return Objects.hash(employeeInOrder);
    }

    @Override
    public String toString() {
        return "EmployeesInOrder{" +
                "employeesInOrder=" + employeeInOrder +
                '}' + '\n';
    }
}
