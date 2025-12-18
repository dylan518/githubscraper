package com.consumeApi.consumeApi.Model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ItemEntity {
    private PersonaEntity personaEntity;
    private String municipio;

    public String getMunicipioFinal(){
        return personaEntity.getNombre() + " Pertenece a " +municipio;
    }

}
