package bzh.eni.ecole.dal;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;

import bzh.eni.ecole.bo.Personne;
import jakarta.persistence.EntityManager;
import jakarta.persistence.TypedQuery;

public class PersonneDaoImpl implements PersonneDaoCustom {

	@Autowired private EntityManager em;
	
	@Override
	public Personne findPersonneParPrenom(String prenom) {
		TypedQuery<Personne> tQuery= em.createQuery("SELECT p FROM Personne p WHERE p.prenom LIKE :prenom",
				Personne.class);
		
		tQuery.setParameter("prenom", "%"+prenom+"%");
		
		return tQuery.getSingleResult();
	}

	@Override
	public Personne trouverUn(Integer id) {		
		return em.createNamedQuery("trouverUn",Personne.class)
				.setParameter("id", id)
				.getSingleResult();
	}


}