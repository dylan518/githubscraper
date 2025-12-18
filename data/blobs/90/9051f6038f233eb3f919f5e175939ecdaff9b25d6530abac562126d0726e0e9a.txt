package br.unitins.topicos1.service;

import java.util.ArrayList;
import java.util.List;

import com.oracle.svm.core.annotate.Inject;

import br.unitins.topicos1.dto.ClienteResponseDTO;
import br.unitins.topicos1.dto.TelefoneDTO;
import br.unitins.topicos1.dto.UsuarioDTO;
import br.unitins.topicos1.dto.UsuarioResponseDTO;
import br.unitins.topicos1.model.Cliente;
import br.unitins.topicos1.model.Perfil;
import br.unitins.topicos1.model.Telefone;
import br.unitins.topicos1.model.Usuario;
import br.unitins.topicos1.repository.UsuarioRepository;
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import validation.ValidationException;

public class UsuarioServiceImpl implements UsuarioService{
    @Inject
    UsuarioRepository repository;
    @Inject
    HashService hashService;

    @Override
    @Transactional
    public UsuarioResponseDTO insert(@Valid UsuarioDTO dto) {

        if (repository.findByLogin(dto.login()) != null) {
            throw new ValidationException("login", "Login já existe.");
        }

        Usuario novoUsuario = new Usuario();
        novoUsuario.setNome(dto.nome());
        novoUsuario.setEmail(dto.email());
        novoUsuario.setLogin(dto.login());
        novoUsuario.setSenha(hashService.getHashSenha(dto.senha()));
        novoUsuario.setPerfil(Perfil.ValueOf(dto.idPerfil()));

        if (dto.agenda() != null && 
                    !dto.agenda().isEmpty()){
            novoUsuario.setAgenda(new ArrayList<Telefone>());
            for (TelefoneDTO tel : dto.agenda()) {
                Telefone telefone = new Telefone();
                telefone.setCodigoArea(tel.codigoArea());
                telefone.setNumero(tel.numero());
                novoUsuario.getAgenda().add(telefone);
            }
        }

        repository.persist(novoUsuario);

        return UsuarioResponseDTO.valueOf(novoUsuario);
    }

    @Override
    public UsuarioResponseDTO update(UsuarioDTO dto, Long id) {
        Usuario usuarioAlterado = repository.findById(id);
        usuarioAlterado.setEmail(dto.email());
        usuarioAlterado.setLogin(dto.login());
        usuarioAlterado.setNome(dto.nome());
        usuarioAlterado.setSenha(dto.senha());

        if (dto.agenda() != null && !dto.agenda().isEmpty()) {
            usuarioAlterado.setAgenda(new ArrayList<Telefone>());
            for (TelefoneDTO tel : dto.agenda()) {
                Telefone telefone = new Telefone();
                telefone.setCodigoArea(tel.codigoArea());
                telefone.setNumero(tel.numero());
                usuarioAlterado.getAgenda().add(telefone);
            }
        }

        repository.persist(usuarioAlterado);

        return UsuarioResponseDTO.valueOf(usuarioAlterado); 
    }

    @Override
    @Transactional
    public void delete(Long id) {
    }

    @Override
    public UsuarioResponseDTO findById(Long id) {
        return UsuarioResponseDTO.valueOf(repository.findById(id));
    }

    @Override
    public List<UsuarioResponseDTO> findByNome(String nome) {
        return null;
    }

    @Override
    public UsuarioResponseDTO findByLoginAndSenha(String login, String senha) {
        Usuario usuario = repository.findByLoginAndSenha(login, senha);
        if (usuario == null) 
            throw new ValidationException("login", "Login ou senha inválido");
        
        return UsuarioResponseDTO.valueOf(usuario);
    }

    @Override
    public UsuarioResponseDTO findByLogin(String login) {
        Usuario usuario = repository.findByLogin(login);
        if (usuario == null) 
            throw new ValidationException("login", "Login inválido");
        
        return UsuarioResponseDTO.valueOf(usuario);
    }

    @Override
    public List<UsuarioResponseDTO> findByAll() {
        return repository.listAll().stream()
            .map(e -> UsuarioResponseDTO.valueOf(e)).toList();
}
}
