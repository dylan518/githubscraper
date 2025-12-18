package com.imaginnovate.Controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import com.imaginnovate.Dto.DivisionsDto;
import com.imaginnovate.Entities.Divisions;
import com.imaginnovate.Repository.DivisionsRepo;

import jakarta.inject.Inject;
import jakarta.transaction.Transactional;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.PathParam;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/hello")
public class DivisionController {

    @Inject
    DivisionsRepo divisionsRepo;


   @GET
    @Path("/getall")
    @Produces(MediaType.APPLICATION_JSON)
    public List<DivisionsDto> all() {
        List<Divisions> divisions = Divisions.listAll();
        List<DivisionsDto> divisionsDtos = new ArrayList<>();
        for (Divisions d : divisions) {
            DivisionsDto dto = new DivisionsDto();
            dto.setId(d.getId()); 
            dto.setName(d.name);
            if (d.parent != null) {
                dto.setParent(d.parent.getId()); 
            }
            divisionsDtos.add(dto);
        }
        return divisionsDtos;
    }



    @POST
    @Path("/add")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    @Transactional
    public Response createDivision(DivisionsDto divisionsDto) {
        Divisions division = new Divisions();
        division.name = divisionsDto.getName();
        if (divisionsDto.getParent() != 0) {
            Optional<Divisions> parentOpt = divisionsRepo.findByIdOptional(divisionsDto.getParent());
            if (parentOpt.isPresent()) {
                division.parent = parentOpt.get(); 
            }
        }

        divisionsDto.setId(division.getId()); 
        divisionsRepo.persist(division); 
        return Response.status(Response.Status.CREATED).entity(divisionsDto).build();
    }



    @GET
    @Path("/get/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public DivisionsDto getById(@PathParam("id") int id) {
        Divisions division = divisionsRepo.findById(id);
        if (division == null) {
            return null;
        }
        DivisionsDto divisionDto = new DivisionsDto();
        divisionDto.setId(division.getId()); 
        divisionDto.setName(division.name);
        if (division.parent != null) { 
            divisionDto.setParent(division.parent.getId());
        }
        return divisionDto;
    }
    }










