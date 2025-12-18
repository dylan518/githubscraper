package com.example.modern.HMS.entity;

import com.example.modern.HMS.enums.CommunicationType;
import com.example.modern.HMS.enums.MessageStatus;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.ZonedDateTime;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name="compliance")
public class ComplianceAndRegulatory {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Integer id;
    @Column(name = "compliance_id")
    private Integer compliance_id;
    @Column(name = "regulation_type")
    private String regulation_type;
    @Column(name = "description")
    private String description;
    @Column(name = "compliance_status")
    private String compliance_status;
    @Column(name = "audit_date")
    private String audit_date;
    @Column(name = "audit_results")
    private String audit_results;
    @Column(name = "corrective_results")
    private String  corrective_results;
    @Column(name = "created_at")
    private ZonedDateTime created_at;
    @Column(name = "updated_at")
    private ZonedDateTime updated_at;
    @Column(name = "deleted_at")
    private ZonedDateTime deleted_at;
}
