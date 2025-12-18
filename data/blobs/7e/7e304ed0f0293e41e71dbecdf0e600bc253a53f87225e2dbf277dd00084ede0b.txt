package br.com.forumhub.api.domain.topico;

import br.com.forumhub.api.domain.validacao.ValidacaoException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class TopicoService {
    @Autowired
    private TopicoRepository repositorio;

    @Autowired
    private List<ValidadoresTopico> validadores;


    public Topico criar(DadosTopico dados) {

        validadores.forEach(v -> v.validar(dados));

        var topicoNovo = new Topico(null, dados.titulo(), dados.mensagem(), dados.data(), true, dados.curso());

        repositorio.save(topicoNovo);

        return topicoNovo;
    }

    public List<Topico> listar() {
        return repositorio.findAll();
    }

    public Optional<Topico> detalhar(Long id) {
        return repositorio.findById(id);
    }


    public Topico atualizar(Long id, DadosTopico dados) {
        Optional<Topico> topicoOptional = repositorio.findById(id);

        if (topicoOptional.isPresent()) {
            validadores.forEach(v -> v.validar(dados));
            Topico topico = topicoOptional.get();
            topico.atualizar(dados);
            repositorio.save(topico);
            return topico;
        }
        else{
            throw new ValidacaoException("Tópico com esse id não encontrado");
        }
    }

    public void apagar(Long id) {
        Optional<Topico> topicoOptional = repositorio.findById(id);

        if (topicoOptional.isPresent()) {
            repositorio.deleteById(id);
        } else {
            throw new ValidacaoException("Tópico com esse id não encontrado");
        }
    }

}
