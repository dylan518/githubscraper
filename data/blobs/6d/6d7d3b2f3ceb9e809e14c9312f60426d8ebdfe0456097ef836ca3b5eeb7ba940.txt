package com.sena.prueba.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sena.prueba.interfaceService.IclienteService;
import com.sena.prueba.interfaces.Icliente;
import com.sena.prueba.model.cliente;
import com.sena.prueba.model.estado;

@Service
public class clienteService implements IclienteService{

    @Autowired
    private Icliente data;
    
    @Override
	public String save(cliente cliente) {
		data.save(cliente);
		return cliente.getId_cliente();
	}

    @Override
	public List<cliente> findAll() {
		List<cliente> listacliente=
				(List<cliente>) data.findAll();
		//(List<cliente>) : Es un cast
		//ya que findAll() retorna un objeto distinto
		//- Retorna un iterable <cliente>
		//- se convierte a list <cliente>
		return listacliente;
	}
	@Override
	public List<cliente> filtrocliente(String filtro) {
		List<cliente>Listacliente=data.filtrocliente(filtro);
		return Listacliente;
	}
	@Override
	public List<cliente> filtroClientePorEstado(estado estado) {
		List<cliente>Listacliente=data.filtroClientePorEstado(estado);
		return Listacliente;
	}
	
    @Override
	public Optional<cliente> findOne(String id) {
		Optional<cliente> cliente=data.findById(id);
		return cliente;
	}
	
	@Override
	public int delete(String id) {
		data.deleteById(id);
		return 1;
	}
	// @Override
	// public int deletePermanente(String id_cliente) {
	// 	var cliente = data.findById(id_cliente).get();
	// 	cliente.setEstado(estado.Inactivo);
	// 	data.save(cliente); 
	// 	return 0;
	// }
}
