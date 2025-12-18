package com.demo.ecommerce.controller;

import com.demo.ecommerce.model.Produit;
import com.demo.ecommerce.model.Stock;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@WebServlet("/admin")
public class AdminServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        ArrayList<Produit> produits = Stock.getStock().getProduits();

        request.setAttribute("produits", produits);
        request.getRequestDispatcher("WEB-INF/admin.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        ArrayList<Produit> produits = Stock.getStock().getProduits();
        String nom = request.getParameter("nom");
        double prix = Double.parseDouble(request.getParameter("prix"));

        Produit nouveauProduit = new Produit(nom, prix);
        produits.add(nouveauProduit);

        response.sendRedirect(request.getContextPath() + "/admin");
    }
}
