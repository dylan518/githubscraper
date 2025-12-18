package marwa.userservice;
import marwa.userservice.entities.User;
import marwa.userservice.enums.UserRole;
import marwa.userservice.repo.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class UserServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(UserServiceApplication.class, args);
	}

	@Bean
	CommandLineRunner start(UserRepository userRepository) {
		return args -> {
			User user1 = User.builder()
					.nom("Triaa")
					.prenom("Marwa")
					.mail("user1@mail.com")
					.mdp("password1")
					.role(UserRole.SCRUM_MASTER)
					.build();

			// Enregistrer le nouvel utilisateur
			userRepository.save(user1);

			User user2 = User.builder()
					.nom("Nom2")
					.prenom("Prenom2")
					.mail("user2@mail.com")
					.mdp("password2")
					.role(UserRole.DEVELOPER)
					.build();

			// Enregistrer le nouvel utilisateur
			userRepository.save(user2);

			// Afficher tous les utilisateurs
			userRepository.findAll().forEach(System.out::println);
		};
	}
}
