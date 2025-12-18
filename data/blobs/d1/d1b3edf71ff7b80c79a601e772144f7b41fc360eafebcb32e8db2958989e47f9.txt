package examples.spring_boot.test_application;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.test.context.TestConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.containers.output.Slf4jLogConsumer;

import java.util.Collections;
import java.util.Map;

@TestConfiguration(proxyBeanMethods = false)
@ConfigurationProperties("environment")
@Slf4j
public class TestcontainersConfiguration {
    private static final PostgreSQLContainer<?> postgresContainer = new PostgreSQLContainer<>("postgres:16.4-alpine3.20")
            .withDatabaseName("testdb")
            .withUsername("testuser")
            .withPassword("testpassword");

    static {
        // Starten des Containers, bevor die Properties gesetzt werden
        postgresContainer.start();
    }

    private Map<String, String> environment = Collections.emptyMap();

    /**
     * @param registry Die DynamicPropertyRegistry, die die Properties zur Laufzeit setzt.
     */
    @DynamicPropertySource
    static void registerPgProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", postgresContainer::getJdbcUrl);
        registry.add("spring.datasource.username", postgresContainer::getUsername);
        registry.add("spring.datasource.password", postgresContainer::getPassword);
        registry.add("spring.datasource.driver-class-name", postgresContainer::getDriverClassName);
    }

    @Bean
    public GenericContainer<?> myUpstreamApp() {
        // PostgreSQL-Datenbankinformationen dynamisch aus dem PostgreSQL-Container
        GenericContainer<?> upstreamApp = new GenericContainer<>("alpine:latest")
                .withEnv("DB_HOST", postgresContainer.getHost())
                .withEnv("DB_PORT", postgresContainer.getMappedPort(5432).toString())
                .withEnv("DB_NAME", postgresContainer.getDatabaseName())
                .withEnv("DB_USER", postgresContainer.getUsername())
                .withEnv("DB_PASSWORD", postgresContainer.getPassword())
                .withEnv(environment)
                .withCommand("sh", "-c", "env && echo World && sleep 3000");

        upstreamApp.start();

        // Verfolgen der Logs des Containers
        Slf4jLogConsumer logConsumer = new Slf4jLogConsumer(log);
        upstreamApp.followOutput(logConsumer);

        return upstreamApp;
    }
}