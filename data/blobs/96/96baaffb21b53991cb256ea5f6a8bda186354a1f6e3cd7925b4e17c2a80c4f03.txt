package com.cursoloiane.estruturasdados.listaEncadeada;

public class ListaEncadeada<T> {

    private No<T> inicio;
    private No<T> ultimo;
    private int tamanho;

    public void adiciona(T elemento) {
        No<T> celula = new No<T>(elemento);
        if (tamanho == 0) {
            inicio = celula;
        } else {
            ultimo.setProximo(celula);
        }
        ultimo = celula;
        tamanho++;
    }

    public void limpa() {

        for (No<T> atual = inicio; atual != null; ) {
            No<T> proximo = atual.getProximo();
            atual.setElemento(null);
            atual.setProximo(null);
            atual = proximo;
        }
        inicio = null;
        ultimo = null;
        tamanho = 0;
    }

    public int getTamanho() {
        return tamanho;
    }

    @Override
    public String toString() {
        if (tamanho == 0) {
            return "[]";
        }
        StringBuilder saida = new StringBuilder("[");
        No<T> atual = inicio;

        for (int i = 0; i < tamanho - 1; i++) {
            saida.append(atual.getElemento()).append(",");
            atual = atual.getProximo();
        }
        saida.append(atual.getElemento()).append("]");
        return saida.toString();
    }
}