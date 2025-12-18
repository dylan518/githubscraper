package tn.esprit.com.entities;


import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.Date;
import java.util.List;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Skieur {
    @Id
    @Column(name = "IDskieur")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long numSkieur;
    @Column(name = "nomS")
    private String nomS;
    @Column(name = "prenomS")
    private String prenomS;
    @Column(name = "dateNaissance")
    private Date dateNaissance;
    @Column(name = "ville")
    private String ville;
    @ManyToMany
    private List<Piste> pistes;
    @OneToOne
    private Abonnement abonnement;
    @OneToMany
    private List<Inscription> inscriptions;

}
