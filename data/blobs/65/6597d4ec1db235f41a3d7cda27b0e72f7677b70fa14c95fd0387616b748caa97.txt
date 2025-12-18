/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package com.atmProject.servlet;

import com.atmProject.database.DatabaseConnection;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 *
 * @author khatr
 */
public class fastCashServlet extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException, SQLException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            String one = request.getParameter("fiveh");
//           int fiveHundred = Integer.parseInt(request.getParameter("fiveh"));
//int onethousand = Integer.parseInt(request.getParameter("onet"));
//int fivethousand = Integer.parseInt(request.getParameter("fivet"));
//int tenthousand = Integer.parseInt(request.getParameter("tent"));
//int twentythousand = Integer.parseInt(request.getParameter("twentyt"));
            Connection cn = DatabaseConnection.getConnection();
            String fivehundred = request.getParameter("fiveh");
            int amount = 0;
            amount = 500;
            Statement stmt = cn.createStatement();
            ResultSet rs = stmt.executeQuery("select * from login");
            while (rs.next()) {
                int cardno = rs.getInt("cardno");
                String updateQuery = "update login set Balance = Balance -'" + amount + "' where cardno = '" + cardno + "'";
                cn.prepareStatement(updateQuery).execute();
                RequestDispatcher rd = request.getRequestDispatcher("withdraw.jsp");
                rd.include(request, response);
                System.out.println("True");
                out.print("<h1>!!!You withdraw Rs: " + amount + ". Please collect your cash!!! </h1>");
            }
        }
    }
}
