package com.businesscase.software_engineering.application.tasks.exceptions;

public class TaskNotFoundByParam extends RuntimeException {

    private final String parametro;

    public TaskNotFoundByParam(String parametro) {
        super(String.format("Task não encontrada para o parâmetro de busca: %s", parametro));
        this.parametro = parametro;
    }

    public String getParametro() {
        return parametro;
    }
}
