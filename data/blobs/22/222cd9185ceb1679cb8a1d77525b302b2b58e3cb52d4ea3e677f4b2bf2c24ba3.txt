
package com.rest;

import com.model.User;
import com.model.Users;

import com.model.dao.SQLConnector;
import com.model.dao.UserSqlDAO;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.SQLException;
import java.util.List;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import javax.xml.bind.JAXBException;


@Path("sqlapi")
public class UserSqlService {
    
    @GET
    @Path("users") //http://localhost:8080/demo/rest/sqlapi/users
    @Produces(MediaType.APPLICATION_XML)
    public Users getUsers() throws JAXBException, FileNotFoundException, ClassNotFoundException, SQLException, InstantiationException, IllegalAccessException, IOException {
        UserSqlDAO userSqlDAO = new UserSqlDAO(new SQLConnector().connection());
        Users users = new Users();
        users.addAll(userSqlDAO.getUsers());
        return users;
    }

    @GET
    @Path("user/ID/{ID}") //http://localhost:8080/demo/rest/sqlapi/user/ID/100000
    @Produces(MediaType.APPLICATION_XML)
    public Users getUser(@PathParam("ID") int ID) throws JAXBException, FileNotFoundException, ClassNotFoundException, SQLException, InstantiationException, IllegalAccessException, IOException {
        UserSqlDAO userSqlDAO = new UserSqlDAO(new SQLConnector().connection());
       
        User user = userSqlDAO.getUser(ID);
        Users users = new Users();
        users.add(user);
        return users;
    }

    @GET
    @Path("user") //http://localhost:8080/demo/rest/sqlapi/user?ID=100000
    @Produces(MediaType.APPLICATION_XML)
    public Users fetchUser(@QueryParam("ID") int ID) throws JAXBException, FileNotFoundException, ClassNotFoundException, SQLException, InstantiationException, IllegalAccessException, IOException {
        UserSqlDAO userSqlDAO = new UserSqlDAO(new SQLConnector().connection());
       
        User user = userSqlDAO.getUser(ID);
        Users users = new Users();
        users.add(user);
        return users;
    }
}

