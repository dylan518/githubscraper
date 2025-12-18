package uchuca.domain.serviceImp;


import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.stereotype.Service;

import uchuca.domain.AsignacionEtiquetas;
import uchuca.domain.repository.AsignacionEtiquetasRepository;


import java.util.List;
import java.util.Optional;
@Service
public class AsignacionEtiquetasService {

    @Autowired
    private AsignacionEtiquetasRepository repository;

    public Optional<AsignacionEtiquetas> getId(Integer id){
        return repository.getId(id);
    }

    public List<AsignacionEtiquetas> getAll(){
        return repository.getAll();
    }

    public AsignacionEtiquetas save(AsignacionEtiquetas asignacionEtiquetas){
        return repository.save(asignacionEtiquetas);
    }
}
