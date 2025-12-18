/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package backenddmn20222.models.beans;

/**
 *
 * @author lab04aluno
 */
public class Logradouro {
    
    int id;
    String endereco;
    String cep;
    String Complemento;

    public Logradouro(int id) {
        this.id = id;
    }

    public Logradouro(String endereco) {
        this.endereco = endereco;
    }

 
    public Logradouro(String endereco, String cep, String Complemento) {
        this.endereco = endereco;
        this.cep = cep;
        this.Complemento = Complemento;
    }

    public Logradouro(int id, String endereco, String cep, String Complemento) {
        this.id = id;
        this.endereco = endereco;
        this.cep = cep;
        this.Complemento = Complemento;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getEnd() {
        return endereco;
    }

    public void setEnd(String endereco) {
        this.endereco = endereco;
    }

    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }

    public String getComp() {
        return Complemento;
    }

    public void setComp(String Complemento) {
        this.Complemento = Complemento;
    }

    @Override
    public String toString() {
        return "Logradouro{" + "id=" + id + ", endereco=" + endereco + ", cep=" + cep + ", Complemento=" + Complemento + '}';
    }
    

    
}

