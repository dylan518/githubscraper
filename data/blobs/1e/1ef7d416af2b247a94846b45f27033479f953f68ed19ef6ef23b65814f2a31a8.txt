package entity.Services;

import base.entity.BaseEntity;
import entity.Order;
import entity.users.Expert;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.List;

@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
@AllArgsConstructor
@NoArgsConstructor
@Data
@Table(name = "sub_services")
public class SubServiceCollection extends BaseEntity<Long> {
    String name;
    @ManyToOne
    ServiceCollection service;
    int basePrice;
    String caption;
    @ManyToMany
    List<Expert> Experts;
    @OneToOne(mappedBy = "subServiceCollection")
    Order order;

    public SubServiceCollection(String name, int basePrice, String caption) {
        this.name = name;
        this.basePrice = basePrice;
        this.caption = caption;
    }

    @Override
    public String toString() {
        return "SubServiceCollection{" +
                "name='" + name + '\'' +
                ", service=" + service.getName() +
                ", basePrice=" + basePrice +
                ", caption='" + caption + '\'' +
                ", Experts=" + Experts +
                ", order=" + order +
                '}';
    }

    public SubServiceCollection(String name, ServiceCollection service, int basePrice, String caption) {
        this.name = name;
        this.service = service;
        this.basePrice = basePrice;
        this.caption = caption;
    }
}
