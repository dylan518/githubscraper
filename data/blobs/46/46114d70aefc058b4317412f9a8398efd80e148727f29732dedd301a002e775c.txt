package com.amigo_oculto.api.Aplicattion.use_cases.implementation;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.amigo_oculto.api.Aplicattion.abstration_gateway.SorteioGateway;
import com.amigo_oculto.api.Aplicattion.use_cases.abstration.InterfaceGerenciarSorteio;
import com.amigo_oculto.api.entities.Sorteio;




@Component
public class GerenciarSorteios  implements InterfaceGerenciarSorteio {

    private final SorteioGateway repository;

    public GerenciarSorteios(SorteioGateway repository) {
        this.repository = repository;
    }

    public Sorteio criar(Sorteio evento) {
        return repository.salvar(evento);
    }

    public List<Sorteio> listar() {
        return repository.listarTodos();
    }

    public Optional<Sorteio> buscarPorId(Long id) {
        return repository.buscarPorId(id);
    }

    public Sorteio atualizar(Long id, Sorteio sorteioAtualizado) {
        return repository.buscarPorId(id).map(sorteio -> {
            Sorteio atualizado = new Sorteio(
                sorteio.getId(),
                sorteioAtualizado.getEventoId(),
                sorteioAtualizado.getDoadorId(),
                sorteioAtualizado.getReceptorId()  
            );
            return repository.salvar(atualizado);
        }).orElseThrow(() -> new RuntimeException("Produto não encontrado"));


      

    }

    public void deletar(Long id) {
        repository.deletar(id);
    }

}
