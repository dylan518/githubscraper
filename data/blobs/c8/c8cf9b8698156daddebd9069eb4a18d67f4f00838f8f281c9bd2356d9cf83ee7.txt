package com.asignarEquipo.asignarEquipo.service;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;
import com.asignarEquipo.asignarEquipo.model.Equipo;
import com.asignarEquipo.asignarEquipo.repositories.EquipoRepository;

@Service("equipoService")
public class EquipoServiceImpl implements EquipoService {

    @Autowired
    protected EquipoRepository equipoRepository;

    @Override
    public Equipo buscarId(Long id) {
        Equipo equipoData = equipoRepository.buscarId(id);

        return equipoData;

    }

    @Override
    public List<Equipo> listar() {
        return equipoRepository.findAll();
    }

    @Override
    public List<Equipo> buscar(String filtro) {
        return equipoRepository.findAllFiltro(filtro);
    }

    @Override
    public Equipo crear(Equipo equipo) {
        return equipoRepository.save(equipo);
    }

    @Override
    public Equipo actualizar(Long id, Equipo equipo) {
        Equipo equipoData = equipoRepository.buscarId(id);
        Equipo _equipo = equipoData;
        _equipo.setCodigo(equipo.getCodigo());
        _equipo.setMarca(equipo.getMarca());
        _equipo.setRam(equipo.getRam());
        _equipo.setDisco(equipo.getDisco());
        _equipo.setTipo(equipo.getTipo());
        _equipo.setProcesador(equipo.getProcesador());
        _equipo.setFechaCompra(equipo.getFechaCompra());
        return equipoRepository.save(_equipo);

    }

    @Override
    public Boolean eliminar(Long id) {
        try {
            Equipo equipoData = equipoRepository.buscarId(id);
            equipoRepository.delete(equipoData);
            return true;
        } catch (Exception e) {
            return false;
        }

    }
}
