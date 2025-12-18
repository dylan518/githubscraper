package com.evaluation.springboot.model;

import com.evaluation.springboot.mapper.CategoriesEnum;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "category")
public class Category {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column( name = "category_name",nullable = false)
    @Enumerated(EnumType.STRING)
    private CategoriesEnum name;

}
