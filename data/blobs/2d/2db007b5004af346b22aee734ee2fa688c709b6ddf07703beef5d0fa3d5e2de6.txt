package foro.hub.controller;

import foro.hub.domain.topico.*;
import jakarta.transaction.Transactional;
import jakarta.validation.Valid;
import foro.hub.domain.usuarios.Usuario;
import foro.hub.domain.usuarios.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.util.Optional;

@RestController
@RequestMapping("topicos")
public class TopicoController {
    @Autowired
    private TopicoRepository topicoRepository;
    @Autowired
    private UsuarioRepository usuarioRepository;
    @PostMapping
    public ResponseEntity<?> registrarTopicos(@RequestBody @Valid DatosRegistroTopico datosRegistroTopico,
                                                                 UriComponentsBuilder uriComponentsBuilder){
        Optional<Usuario> usuario = usuarioRepository.findById(datosRegistroTopico.idUsuario());
        if(usuario.isPresent()){
            var usuarioEncontrado = usuario.get();
            Topico topico = new Topico(datosRegistroTopico,usuarioEncontrado);
            topicoRepository.save(topico);
            DatosRespuestaTopico datosRespuestaTopico = new DatosRespuestaTopico(topico);
            URI url = uriComponentsBuilder.path("/topicos/{id}").buildAndExpand(topico.getId()).toUri();
            return ResponseEntity.created(url).body(datosRespuestaTopico);

        }else{
            return ResponseEntity.unprocessableEntity().body("Usuario no encontrado");
        }

    }
    @GetMapping
    public ResponseEntity<Page<DatosRespuestaTopico>> listadoTopicos(@PageableDefault(size=2) Pageable paginacion){
        return ResponseEntity.ok(topicoRepository.findByStatusTrue(paginacion).map(DatosRespuestaTopico::new));
    }

    @PutMapping
    @Transactional
    public ResponseEntity actualizarTopicos(@RequestBody @Valid DatosActualizarTopico datosActualizarTopico){
        Topico topico = topicoRepository.getReferenceById(datosActualizarTopico.id());
        topico.actualizarDatos(datosActualizarTopico);
        return ResponseEntity.ok(new DatosRespuestaTopico(topico.getId(),
                topico.getMensaje(), topico.getTitulo(), topico.getFechaCreacion()));
    }

    @DeleteMapping("/{id}")
    @Transactional
    public ResponseEntity eliminarTopico(@PathVariable Long id){
        Topico topico = topicoRepository.getReferenceById(id);
        topico.desactivarTopico();
        return ResponseEntity.noContent().build();
    }

}
