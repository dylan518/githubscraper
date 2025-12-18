package com.elBuenSabor.JPA;

import com.elBuenSabor.JPA.Entidades.Cliente;
import com.elBuenSabor.JPA.Repositorios.ClienteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class JpaApplication {
	@Autowired //Realiza la inyeccion automatica de dependencia
	ClienteRepository clienteRepository;

	public static void main(String[] args) {
		SpringApplication.run(JpaApplication.class, args);
		System.out.println("Estoy funcionando");
	}

@Bean
CommandLineRunner init(ClienteRepository clienteRepo) {
		return args -> {
			System.out.println("<-----FUNCIONANDO----->");
			Cliente cliente = new Cliente();
			cliente.setNombre("Luciano");
			cliente.setApellido("Bazaes");
			cliente.setTelefono("123456789");
			cliente.setEmail("lucianobzs@email.com");

			clienteRepository.save(cliente);

		};
}

}

