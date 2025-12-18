package com.mycompany.tacotitosv2.Modelos;

public class Ingrediente{
    protected int id;
    public tipoIngrediente tipo;
    protected int tipo_id;
    protected String nombre;
    protected double precio;
    
    public Ingrediente (int id, String nombre, double precio, int tipoID){
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.tipo_id = tipoID;
    }
    
    /*public Ingrediente(String nombre, double precio, int tipoID){
        this.nombre = nombre;
        this.precio = precio;
        this.tipo_id = tipoID;
    }*/
    
    public int getTipo_ID(){
        return this.tipo_id;
    }
    public int getId(){
        return id;
    }
    public void setId(int id){
        this.id = id;
    }
    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public double getPrecio() {
        return precio;
    }
    
    public void setPrecio(double precio) {
        this.precio = precio;
    }
    @Override
    public String toString() {
        return super.toString() + "Ingrediente{" + "nombre=" + nombre + ", precio=" + precio + '}';
    }
    public Ingrediente(){
    }
}
