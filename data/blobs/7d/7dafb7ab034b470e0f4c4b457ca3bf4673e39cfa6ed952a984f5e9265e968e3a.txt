package tn.esprit.yossr_bessaad_4se.entities;


import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.Set;


@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Entity
public class Skier implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
     Long numSkier;
      String firstName;
     String lastName;
    @Column(nullable = false)
     LocalDate dateOfBirth;
     String city;

    @OneToOne(cascade ={ CascadeType.PERSIST,CascadeType.REMOVE})
    Subscription subscription;

    @OneToMany(mappedBy = "skier" , fetch = FetchType.EAGER)
    Set<Registration> registrations;


    @ManyToMany(mappedBy = "skiers")
    Set<Piste>pistes;
}
