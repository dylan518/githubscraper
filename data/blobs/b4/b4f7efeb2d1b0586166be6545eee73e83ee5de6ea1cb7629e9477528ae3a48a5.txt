package com.incom.model;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import javax.validation.constraints.NotNull;

import org.hibernate.annotations.CreationTimestamp;

import com.fasterxml.jackson.annotation.JsonIdentityInfo;
import com.fasterxml.jackson.annotation.ObjectIdGenerators;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonIdentityInfo(generator = ObjectIdGenerators.IntSequenceGenerator.class)
public class SalesOrder {

    /** ID */
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    /** 顧客 */
    @ManyToOne
    @EqualsAndHashCode.Exclude
    private Customer customer;

    /** 注文日 */
    @CreationTimestamp
    private LocalDate orderDate;

    /** 納品日 */
    @NotNull
    private LocalDate deliveryDate;

    /** 返却日 */
    @NotNull
    private LocalDate returnDate;

    /** 納品先 */
    @NotNull
    @ManyToOne
    private Address address;

    /** 注文商品リスト */
    @OneToMany(mappedBy = "salesOrder", cascade = CascadeType.ALL)
    private List<SalesOrderDetail> salesOrderDetails = new ArrayList<SalesOrderDetail>();

    /** 注文商品リスト */
    public void setSalesOrderDetails(List<SalesOrderDetail> salesOrderDetails) {
        this.salesOrderDetails = salesOrderDetails;
        if (salesOrderDetails != null) {
            for (SalesOrderDetail salesOrderDetail : salesOrderDetails) {
                salesOrderDetail.setSalesOrder(this);
            }
        }
    }

    /** 注文商品リスト */
    public void addSalesOrderDetails(SalesOrderDetail salesOrderDetail) {
        this.salesOrderDetails.add(salesOrderDetail);
        salesOrderDetail.setSalesOrder(this);
    }
}
