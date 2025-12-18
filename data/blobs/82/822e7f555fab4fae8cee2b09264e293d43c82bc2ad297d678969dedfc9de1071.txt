package org.example.dao.impl;

import org.example.dao.BookDao;
import org.example.models.Livre;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;

public class BookDaoImpl implements BookDao {

    private List<Livre> livres;

    public BookDaoImpl(){
        livres = new ArrayList<>();
    }

    @Override
    public void createBook(Livre livre) {
        livres.add(livre);
    }

    @Override
    public void updateBook(Livre livre, int id_livre) {
        //recuperation de l'element
        Livre old_livre = this.getBookById(id_livre);

        if(old_livre != null){
            //recuperation de l'index
            int indexOldLivre = livres.indexOf(old_livre);

            old_livre.setEditeur(livre.getEditeur());
            old_livre.setResume(livre.getResume());
            old_livre.setTitre(livre.getTitre());
            livres.set(indexOldLivre,old_livre);
        }
    }

    @Override
    public Livre getBookById(int id_livre) {
        for(Livre livre : livres){
            if(livre.getId_livre() == id_livre) return livre;
        }
        return null;
    }


    @Override
    public List<Livre> getAllBook() {
        return livres;
    }

    @Override
    public void deleteBook(int id_livre) {
        livres.removeIf(livre -> livre.getId_livre() == id_livre);
    }
}
