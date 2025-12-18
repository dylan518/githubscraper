package com.example.Fraud.Service.controller;

import com.example.Fraud.Service.TarjetaService;
import com.example.Fraud.Service.api.TarjetaApi;
import com.example.Fraud.Service.model.ErrorResponse;
import com.example.Fraud.Service.model.TarjetaDto;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TarjetaController implements TarjetaApi {

    private final TarjetaService tarjetaService;

    public TarjetaController(TarjetaService tarjetaService) {
        this.tarjetaService = tarjetaService;
    }

    @Override
    public ResponseEntity<String> verificarTarjeta(TarjetaDto tarjetaDto) {
        String numeroTarjeta = tarjetaDto.getNumeroTarjeta();
        if (tarjetaService.estaEnListaNegra(numeroTarjeta)) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body(new ErrorResponse("La tarjeta está en la lista negra").toString());
        }
        return ResponseEntity.ok("La tarjeta no está en la lista negra");
    }

    @Override
    public ResponseEntity<List<String>> obtenerListaNegra() {
        List<String> listaNegra = tarjetaService.obtenerListaNegra();
        return ResponseEntity.ok(listaNegra);
    }
}