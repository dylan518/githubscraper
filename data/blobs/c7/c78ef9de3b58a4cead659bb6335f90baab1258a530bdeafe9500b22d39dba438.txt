package com.cee.tech.api.rest.endpoints;

import com.cee.tech.app.bean.userbean.BookTicketI;
import com.cee.tech.app.model.entity.BookTicket;
import com.cee.tech.app.model.entity.Fixture;

import javax.annotation.security.RolesAllowed;
import javax.ejb.EJB;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.List;

@Path("/bookticket")
public class BookTicketRestApi extends BaseRestApi{

    @EJB
    private BookTicketI bookTicketI;

    @Path("/add")
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response add(BookTicket bookTicket) {
        bookTicket = bookTicketI.addOrUpdate(bookTicket);
        return respond();
    }


    @Path("/list")
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response list() {
        return respond(bookTicketI.list(new BookTicket()));
    }

    @Path("/list/ticket/{id}")
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchOneTicket(@PathParam("id") int id) {
        BookTicket oneTicket =  bookTicketI.selectSingle(BookTicket.class,id);
        return respond(oneTicket);
    }


    @Path("/list/{userId}")
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response fetchById(@PathParam("userId") int userId) {
      List<BookTicket> tickets =  bookTicketI.findAllTicketsByUser(userId);
        return respond(tickets);
    }

    @Path("/delete/{ticketId}")
    @DELETE
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response delete(@PathParam("ticketId") int ticketId) {
        bookTicketI.delete(BookTicket.class, ticketId);
        return respond();
    }

}
