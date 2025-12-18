package mesMachines;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Machine {
    private LocalDate dateAchat;
    private String marque;
    private String modele;

    public Machine(LocalDate dateAchat, String marque, String modele) {
        this.dateAchat = dateAchat;
        this.marque = marque;
        this.modele = modele;
    }

    public long getAge() {
        return ChronoUnit.YEARS.between(dateAchat, LocalDate.now());
    }

    /**
     * {@inheritDoc} * @see java.lang.Object#toString()
     */
    @Override
    public String toString() {
        long age = getAge();
        return marque + " " + modele + " (" + age + " an" + (age > 1 ? "s" : "") + ")";
    }
}