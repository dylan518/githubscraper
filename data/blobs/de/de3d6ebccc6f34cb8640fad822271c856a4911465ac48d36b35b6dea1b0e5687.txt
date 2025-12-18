package thomas.backendteknoland.service.impl;

import thomas.backendteknoland.bo.Membre;
import thomas.backendteknoland.repository.MembreRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Profile;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import thomas.backendteknoland.service.MembreService;

import java.util.List;

@Service
@Profile("prod")
public class MembreServiceJpaImpl implements MembreService {

    @Autowired
    private MembreRepository membreRepository;

    @Autowired
    PasswordEncoder passwordEncoder; // utilitaire d'encodage des mots de passe

    @Override
    public void addMembre(Membre membre) throws Exception {
        String motDePasseEncode = passwordEncoder.encode(membre.getPassword());
        membre.setPassword(motDePasseEncode);
        membreRepository.save(membre);
    }

    @Override
    public List<Membre> listeMembres() {
        return membreRepository.findAll();
    }

    @Override
    public Membre getMembreByPseudo(String pseudo) {
        return membreRepository.findById(pseudo).get();
    }
}
