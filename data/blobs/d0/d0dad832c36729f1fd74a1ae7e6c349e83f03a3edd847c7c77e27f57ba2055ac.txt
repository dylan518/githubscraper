package com.hexagonal.infraestructure.entities;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "customer")
@Getter
@AllArgsConstructor
@NoArgsConstructor
public class CustomerEntity {

    @Id
    @Column(columnDefinition = "uuid")
    private UUID id;

    @Column(name = "full_name")
    private String fullName;

    @OneToOne(fetch = FetchType.LAZY)
    @MapsId
    private AccountEntity account;

    @Column(name = "created_at")
    @CreationTimestamp
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    @UpdateTimestamp
    private LocalDateTime updatedAt;

}
