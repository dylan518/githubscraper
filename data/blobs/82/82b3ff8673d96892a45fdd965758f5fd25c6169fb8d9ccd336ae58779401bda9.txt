package com.ProyectoTDSBackend.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ProyectoTDSBackend.dto.ResidenciaDto;
import com.ProyectoTDSBackend.models.Residencia;
import com.ProyectoTDSBackend.repository.ResidenciaRepository;
import com.ProyectoTDSBackend.util.GenericResponse;
import com.ProyectoTDSBackend.util.ParametersApp;

@Service
public class ResidenciaService {

    private static final Logger log = LoggerFactory.getLogger(ResidenciaService.class);

    @Autowired
    private ResidenciaRepository recidenciaRepository;

    public GenericResponse<String> saveRecidencia(ResidenciaDto recidenciaDto) {
        GenericResponse<String> response = new GenericResponse<>();
        try {
            Residencia recidencia = new Residencia();
            //recidencia.setIdRecidencia(recidenciaDto.getIdRecidencia());
            recidencia.setPais(recidenciaDto.getPais());
            recidencia.setNacionalidad(recidenciaDto.getNacionalidad());
            recidencia.setProvincia(recidenciaDto.getProvincia());
            recidencia.setCanton(recidenciaDto.getCanton());
            recidencia.setParroquia(recidenciaDto.getParroquia());
            recidencia.setBarrio(recidenciaDto.getBarrio());
            recidencia.setZona(recidenciaDto.getZona());
            recidencia.setIdUsuario(recidenciaDto.getIdUsuario());
            recidenciaRepository.save(recidencia);
            response.setMessage(ParametersApp.SUCCESSFUL.getReasonPhrase());
            response.setObject(recidencia.getIdRecidencia() + " RECIDENCIA guardado correctamente ");
            response.setStatus(ParametersApp.SUCCESSFUL.value());
        } catch (Exception e) {
            log.error("ERROR", e);
            response.setStatus(ParametersApp.SERVER_ERROR.value());
        }
        return response;
    }

    public GenericResponse<String> updateRecidencia(ResidenciaDto recidenciaDto) {
        GenericResponse<String> response = new GenericResponse<String>();
        try {
            Residencia recidencia = recidenciaRepository.findById(recidenciaDto.getIdRecidencia()).get();
            if (recidencia != null) {
                recidencia.setPais(recidenciaDto.getPais());
                recidencia.setNacionalidad(recidenciaDto.getNacionalidad());
                recidencia.setProvincia(recidenciaDto.getProvincia());
                recidencia.setCanton(recidenciaDto.getCanton());
                recidencia.setParroquia(recidenciaDto.getParroquia());
                recidencia.setBarrio(recidenciaDto.getBarrio());
                recidencia.setZona(recidenciaDto.getZona());
                recidenciaRepository.save(recidencia);
                response.setMessage(ParametersApp.SUCCESSFUL.getReasonPhrase());
                response.setObject("RECIDENCIA " + recidencia.getIdRecidencia() + " actualizado correctamente");
                response.setStatus(ParametersApp.SUCCESSFUL.value());
            }
        } catch (Exception e) {
            log.error("ERROR: ", e);
            response.setStatus(ParametersApp.SERVER_ERROR.value());
        }
        return response;

    }

}
