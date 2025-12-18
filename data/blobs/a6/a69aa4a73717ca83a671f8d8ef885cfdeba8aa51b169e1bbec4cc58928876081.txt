package com.java.chandanahotelandlodging.servlets;

import com.java.chandanahotelandlodging.dataaccessobject.CustomerDAO;
import com.java.chandanahotelandlodging.dataaccessobject.FeedbackDao;
import com.java.chandanahotelandlodging.dataaccessobject.RoomDao;
import com.java.chandanahotelandlodging.entities.Customer;
import com.java.chandanahotelandlodging.entities.Feedback;
import com.java.chandanahotelandlodging.entities.Room;
import com.java.chandanahotelandlodging.helper.FileExploler;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.MultipartConfig;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.Part;
//import jdk.internal.misc.FileSystemOption;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
//import java.io.PrintWriter;

@MultipartConfig
@WebServlet(name = "registerServlet", value = "/registerServlet")
public class RegisterServlet extends HttpServlet
{
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String name = request.getParameter("name");
        String email = request.getParameter("email");
        String phone =  request.getParameter("country_code")+request.getParameter("phone");
        String address = request.getParameter("address");
        String password = request.getParameter("password");
        String type = request.getParameter("type");
        String id_no = request.getParameter("idno");

        Customer c = new Customer(name, email, address, phone, password, null, type, id_no, 0);

        PrintWriter out = response.getWriter();
        try
        {
            CustomerDAO.deleteCustomer(email);
            if(CustomerDAO.saveCustomer(c)){
                out.println("Success");
            } else{
                out.println("Failure");
            }
        }
        catch (Exception e)
        {
            e.printStackTrace();
            out.println("Failure");
        }
    }
}
