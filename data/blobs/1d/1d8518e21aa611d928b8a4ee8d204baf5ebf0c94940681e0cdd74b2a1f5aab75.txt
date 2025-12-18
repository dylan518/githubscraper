package dev.pantanal.grupo2.features.collaborator;

import java.util.Collection;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/collaborator")
public class CollaboratorController {
  @Autowired
  private CollaboratorRepository repository;

  @GetMapping
  public Collection<Collaborator> getAllCollaborators() {
    return this.repository.findAll();
  }

  @GetMapping(path = "/{id}")
  public ResponseEntity<Collaborator> getCollaborator(@PathVariable(value = "id", required = true) String id) {
    var collaborator = this.repository.findById(id);

    if(collaborator.isPresent()) return ResponseEntity.ok(collaborator.get());

    return ResponseEntity.notFound().build();
  }

  @PostMapping
  public ResponseEntity<Collaborator> createCollaborator(@RequestBody(required = true) Collaborator collaborator) {
    this.repository.save(collaborator);

    return ResponseEntity.status(HttpStatus.CREATED).body(collaborator);
  }

  @DeleteMapping(path = "/{id}")
  public ResponseEntity<?> deleteCollaborator(@PathVariable(value = "id", required = true) String id) {
    var collaborator = this.repository.findById(id);

    if(collaborator.isPresent()) {
      this.repository.delete(collaborator.get());
      return ResponseEntity.ok().build();
    }

    return ResponseEntity.notFound().build();
  }
}
