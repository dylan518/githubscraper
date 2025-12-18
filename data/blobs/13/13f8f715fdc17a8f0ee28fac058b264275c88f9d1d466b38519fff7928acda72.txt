package br.edu.ifrs.restina.dev1.grupo1.projetoCinemav2.MapeamentoManyToOne.infrastructure.repository;

import br.edu.ifrs.restina.dev1.grupo1.projetoCinemav2.MapeamentoManyToOne.domain.model.Orcamento;
import br.edu.ifrs.restina.dev1.grupo1.projetoCinemav2.MapeamentoManyToOne.domain.repository.OrcamentoRepository;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.List;

@Component
public class OrcamentoRepositoryImpl implements OrcamentoRepository {
    @PersistenceContext
    private EntityManager manager;

    @Override
    public List<Orcamento> listar() {
        return manager.createQuery("from Orcamento", Orcamento.class)
                .getResultList();
    }

    @Override
    public Orcamento buscar(Long id) {

        return manager.find(Orcamento.class, id);
    }

    @Transactional
    @Override
    public Orcamento salvar(Orcamento orcamento) {

        return manager.merge(orcamento);
    }

    @Transactional
    @Override
    public void remover(Orcamento orcamento) {
        orcamento = buscar(orcamento.getId());
        manager.remove(orcamento);
    }
}
