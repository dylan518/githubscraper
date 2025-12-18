package org.quarkus.controllers;

import jakarta.inject.Inject;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.core.Response;
import org.jboss.logging.annotations.Pos;
import org.quarkus.dtos.Temperatura;
import org.quarkus.services.TemperaturaService;

import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Path("/temperaturas")
public class TemperaturasResource {

    @Inject
    private TemperaturaService service;

    @GET
    public Temperatura getTemperatura() {
        return new Temperatura("Salta", 10, 5);
    }

    @GET
    @Path("/all")
    public List<Temperatura> getTemperaturas() {
        return service.getTemperaturas();
    }

    @POST
    public Temperatura addTemperaturas(Temperatura temperatura) {
        service.addTemperatura(temperatura);
        return temperatura;
    }

    @GET
    @Path("/maxima")
    public Response getMaxima() {
        return service.isEmpty()
                ? Response.status(404).entity("Lista vacia").build()
                : Response.status(200).entity(service.maxima()).build();
    }

    @GET
    @Path("{ciudad}")
    public Temperatura getCiudad(@PathParam("ciudad") String ciudad) {
        return service.getByName(ciudad)
                .orElseThrow(
                        () -> new NoSuchElementException("No hay registros de " + ciudad)
                );
    }


}
