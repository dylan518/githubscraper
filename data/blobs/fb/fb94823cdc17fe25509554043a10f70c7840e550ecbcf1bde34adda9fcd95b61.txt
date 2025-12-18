package com.lld.bookmyshow.models;

import jakarta.persistence.Id;
import jakarta.persistence.MappedSuperclass;
import java.util.Date;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@MappedSuperclass // Don't create a sep table, instead put its attributes to every child
public class BaseModel {
    @Id
    private Long id;

    private Date createdDate;

    private Date lastModifiedAt;
}
