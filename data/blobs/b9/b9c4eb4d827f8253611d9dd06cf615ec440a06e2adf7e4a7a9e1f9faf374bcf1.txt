package tfc.grupo6.dam.service.impl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import tfc.grupo6.dam.model.entities.Dosis;
import tfc.grupo6.dam.model.persist.dao.DosisDAO;
import tfc.grupo6.dam.service.DosisService;

import java.util.List;

@Service
@Transactional
public class DosisServiceImpl implements DosisService {

    @Autowired
    private DosisDAO dosisDAO;

    @Override
    public Dosis save(Dosis dosis) {
        return dosisDAO.save(dosis);
    }

    @Override
    public void deleteById(int id) {
        dosisDAO.deleteById(id);
    }

    @Override
    public Dosis findById(int id) {
        return dosisDAO.findById(id);
    }

    @Override
    public List<Dosis> findByResidenteId(int residenteId) {
        return dosisDAO.findByResidenteId(residenteId);
    }

    @Override
    public List<Dosis> findByEmpleadoId(int empleadoId) {
        return dosisDAO.findByEmpleadoId(empleadoId);
    }

    @Override
    public Dosis update(Dosis dosis) {
        return dosisDAO.update(dosis);
    }
}

