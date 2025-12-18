package br.com.brunnadornelles.database;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Properties;

public class ConectarBanco {

    private static final String DB_URL;
    private static final String USUARIO;
    private static final String SENHA;

    static {
        Properties prop = new Properties();
        try (InputStream inputStream = ConectarBanco.class.getResourceAsStream("/properties/dados.properties")) {
            prop.load(inputStream);
        } catch (IOException e) {
            throw new RuntimeException("Falha ao carregar o arquivo de propriedades.", e);
        }

        DB_URL = prop.getProperty("prop.server.host");
        USUARIO = prop.getProperty("prop.server.user");
        SENHA = prop.getProperty("prop.server.password");

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            throw new RuntimeException("Driver JDBC não encontrado.", e);
        }
    }

    public static Connection conectar() {
        try {
            return DriverManager.getConnection(DB_URL, USUARIO, SENHA);
        } catch (SQLException e) {
            throw new RuntimeException("Falha ao conectar ao banco de dados.", e);
        }
    }
}
