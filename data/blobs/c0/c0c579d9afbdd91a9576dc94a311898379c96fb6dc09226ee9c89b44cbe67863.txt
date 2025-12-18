/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.builder;

/**
 *
 * @author HP
 */
public abstract class HamburguesaBuilder {
    
    protected Hamburguesa hamburguesa;

    public Hamburguesa getHamburguesa() {
        return hamburguesa;
    }
    
    public void crearNuevaHamburguesa(){
        hamburguesa=new Hamburguesa();
    }
    
    public abstract void buildCarne();
    public abstract void buildPan();
    public abstract void buildAderezos();
    
}
