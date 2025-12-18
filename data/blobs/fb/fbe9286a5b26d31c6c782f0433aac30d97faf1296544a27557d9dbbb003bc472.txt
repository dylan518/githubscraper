/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.prova_poo_2;

/**
 *
 * @author joao3
 */
public class Prato {
    
    private double valor;
    private String nome;
    private Categoria categoria;
    
    public Prato(double valor, String nome, Categoria categoria) {
        setValor(valor);
        setNome(nome);
        setCategoria(categoria);
    }

    public void setValor(double valor) {
        if (valor <= 0) {
            throw new IllegalArgumentException("valor incorreto");
        }
        this.valor = valor;
    }

    public void setNome(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            throw new IllegalArgumentException("o campo não pode ser vazio");
        }
        this.nome = nome;
    }

    public void setCategoria(Categoria categoria) {
        if (categoria == null) {
            throw new IllegalArgumentException("categoria invalida");
        }
        this.categoria = categoria;
    }

    public double getValor() {
        return valor;
    }

    public String getNome() {
        return nome;
    }

    public Categoria getCategoria() {
        return categoria;
    }
}
