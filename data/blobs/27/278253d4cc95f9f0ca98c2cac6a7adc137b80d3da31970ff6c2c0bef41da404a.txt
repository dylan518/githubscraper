package it.corso.service;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import it.corso.dao.DettaglioLibroDao;
import it.corso.dao.RecensioneDao;
import it.corso.dao.UtenteDao;
import it.corso.model.DettaglioLibro;
import it.corso.model.Recensione;
import it.corso.model.Utente;

@Service
public class RecensioneServiceImpl implements RecensioneService {
	@Autowired
	private RecensioneDao recensioneDao;
	@Autowired
	private UtenteDao utenteDao;
	@Autowired
	private DettaglioLibroDao dettaglioLibroDao;
	
	// passo in input il commento della recensione, l'username, il ranked e l'id del libro a cui voglio associare la recensione 
	@Override
	public void registraRecensione(String commento, int utenteId, int ranked, int dettaglioLibroId) 
		{
		Recensione recensioneDaSalvare = new Recensione();
		recensioneDaSalvare.setCommento(commento);
		recensioneDaSalvare.setRanked(ranked);
		// scarico dal database un utente dando in input un utenteid
		Utente utente = utenteDao.findById(utenteId).get();
		recensioneDaSalvare.setUtente(utente);
		// scarico dal database un dettaglilibro dando in input un dettagliolibroid
		DettaglioLibro dettaglioLibro = dettaglioLibroDao.findById(dettaglioLibroId).get();
		recensioneDaSalvare.setDettaglioLibro(dettaglioLibro);
		recensioneDao.save(recensioneDaSalvare);	
	}

	@Override
	public List<Recensione> getRecensioniByLibroId(int libroId) {
		return recensioneDao.findAllByDettaglioLibroId(libroId);
	}

	
	@Override	
	public List<Recensione> getTopTen() {
		List<Recensione> recensioni = recensioneDao.getTopTen();
	    return recensioni;
	}

	@Override
	public List<Recensione> getAllFromUtente(int utenteId) {
		return recensioneDao.findByUtenteId(utenteId);
	}


}

