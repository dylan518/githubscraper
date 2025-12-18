package com.jkbd.optional.flatmap;

import java.util.Optional;

public class OptionalComFlatMap {
    public static void main(String[] args) {

        Pessoa pessoaComEndereco = new Pessoa("Lucas", Optional.of(new Endereco("São Paulo")));
        Pessoa pessoaSemEndereco = new Pessoa("Pedro", Optional.empty());

        // Encadeando Optional com flatMap
        Optional<String> cidadeLucas = pessoaComEndereco.getEndereco()
                .flatMap(endereco -> Optional.ofNullable(endereco.getCidade()));
        System.out.println(cidadeLucas.orElse("Cidade não encontrada"));

        Optional<String> cidadePedro = pessoaSemEndereco.getEndereco()
                .flatMap(endereco -> Optional.ofNullable(endereco.getCidade()));
        System.out.println(cidadePedro.orElse("Cidade não encontrada"));
    }
}
