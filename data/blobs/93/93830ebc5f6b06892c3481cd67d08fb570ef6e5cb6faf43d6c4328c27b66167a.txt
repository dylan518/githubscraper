/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.ibb.model;


import java.util.List;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author trainer
 */

 public class PersonTableModel extends AbstractTableModel {
    private final List<Person> personenListe;
    private final String[] spaltenNamen = {"Vorname", "Nachname", "Stadt","Straße"};

    public PersonTableModel(List<Person> pl) {
        this.personenListe = pl;
    }

    @Override
    public int getRowCount() {
        return personenListe.size();
    }


    public int getColumnCount() {
        return spaltenNamen.length;
    }

    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        Person person = personenListe.get(rowIndex);
        switch (columnIndex) {
            case 0: return person.getFirstname();
            case 1: return person.getLastname();
            case 2: return person.getAddress().getCity();
            case 3: return person.getAddress().getCity();
            
            default: return null;
        }
    }

    @Override
    public String getColumnName(int column) {
        return spaltenNamen[column];
    }
}
