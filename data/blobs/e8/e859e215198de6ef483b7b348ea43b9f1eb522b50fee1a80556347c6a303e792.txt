package org.example.kunden_bestellungen.Kunden;

import org.example.kunden_bestellungen.Bestellungen.Bestellung;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class KundeService {
    @Autowired
    private KundeRepository kundeRepository;

    public Kunde findKundeById(Long id) {
        return kundeRepository.findById(id).orElse(null);
    }

    public boolean existsById(Long id) {
        return kundeRepository.existsById(id);
    }

    public List<Kunde> findAllKunden() {
        return kundeRepository.findAll();
    }

    public long countKunden() {
        return kundeRepository.count();
    }

    public Kunde updateKunde(Long id, Kunde kunde) {
        if (kundeRepository.existsById(id)) {
            Kunde existingKunde = kundeRepository.findById(id).orElse(null);
            if (existingKunde != null) {
                existingKunde.setAdresse(kunde.getAdresse());
                existingKunde.setVorname(kunde.getVorname());
                existingKunde.setName(kunde.getName());
                existingKunde.setPlz(kunde.getPlz());

                return kundeRepository.save(existingKunde);
            }
        }
        return null;
    }

    public Kunde saveKunde(Kunde kunde) {
        return kundeRepository.save(kunde);
    }

    public void deleteKundeById(Long id) {
        kundeRepository.deleteById(id);
    }

    public void deleteAllKunden() {
        kundeRepository.deleteAll();
    }
}