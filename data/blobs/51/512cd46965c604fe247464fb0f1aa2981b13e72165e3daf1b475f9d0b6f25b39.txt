
package com.gft.teste.cielo_teste.vo;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.gft.teste.cielo_teste.model.ListaControleLancamento;
import com.gft.teste.cielo_teste.model.TotalControleLancamento;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class ResponseView {

    private TotalControleLancamento totalControleLancamento;
    private List<ListaControleLancamento> listaControleLancamento = null;
    private Integer indice;
    private Integer tamanhoPagina;
    private Integer totalElements;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    public TotalControleLancamento getTotalControleLancamento() {
        return totalControleLancamento;
    }

    public void setTotalControleLancamento(TotalControleLancamento totalControleLancamento) {
        this.totalControleLancamento = totalControleLancamento;
    }

    public List<ListaControleLancamento> getListaControleLancamento() {
        return listaControleLancamento;
    }

    public void setListaControleLancamento(List<ListaControleLancamento> listaControleLancamento) {
        this.listaControleLancamento = listaControleLancamento;
    }

    public Integer getIndice() {
        return indice;
    }

    public void setIndice(Integer indice) {
        this.indice = indice;
    }

    public Integer getTamanhoPagina() {
        return tamanhoPagina;
    }

    public void setTamanhoPagina(Integer tamanhoPagina) {
        this.tamanhoPagina = tamanhoPagina;
    }

    public Integer getTotalElements() {
        return totalElements;
    }

    public void setTotalElements(Integer totalElements) {
        this.totalElements = totalElements;
    }

    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

}
