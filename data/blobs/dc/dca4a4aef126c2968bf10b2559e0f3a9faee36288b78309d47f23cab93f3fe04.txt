package fr.epsi.jdbc.dao;

import fr.epsi.jdbc.entites.Article;
import fr.epsi.jdbc.entites.Fournisseur;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ArticleDaoJdbc extends DatabaseDao implements ArticleDao {
    @Override
    public List<Article> extraire() {
        ArrayList<Article> articles = new ArrayList<>();

        String sql = "SELECT * FROM ARTICLE;";

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PWD);
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()){
            while (rs.next()){
                Fournisseur f = new FournisseurDaoJdbc().getById(rs.getInt("ID_FOU"));
                articles.add(new Article(rs.getInt("ID"),rs.getString("REF"),rs.getString("DESIGNATION"),rs.getDouble("PRIX"),f));
            }

        } catch (SQLException e) {
            // Handle the exception
            System.out.println("An error occurred: " + e.getMessage());
        }
        return articles;
    }

    @Override
    public void insert(Article article) {
        String sql = "INSERT into ARTICLE (ref, designation, prix, id_fou) values (?,?,?,?);";

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PWD);
             PreparedStatement stmt = conn.prepareStatement(sql,Statement.RETURN_GENERATED_KEYS)){
            stmt.setString(1, article.getRef());
            stmt.setString(2, article.getDesignation());
            stmt.setDouble(3,article.getPrix());
            stmt.setInt(4,article.getFournisseur().getId());

            stmt.executeUpdate();

            try(ResultSet rs = stmt.getGeneratedKeys()){
                if (rs.next()){
                    article.setId(rs.getInt(1));
                }
            }
            catch (SQLException e){
                System.out.println("An error occurred: " + e.getMessage());
            }

        } catch (SQLException e) {
            // Handle the exception
            System.out.println("An error occurred: " + e.getMessage());
        }
    }

    @Override
    public int update(String ref, String nouvelleDesignation) {

        String sql = "UPDATE ARTICLE  SET DESIGNATION = ? Where REF = ?;";

        try (Connection conn = DriverManager.getConnection(DB_URL,DB_USER,DB_PWD);
             PreparedStatement stmt = conn.prepareStatement(sql);) {

            // Set the parameters
            stmt.setString(1, ref);
            stmt.setString(2, nouvelleDesignation);

            // Execute the statement
            return stmt.executeUpdate();

        } catch (SQLException e) {
            // Handle the exception
            System.out.println("An error occurred: " + e.getMessage());
        }
        return 0;
    }

    @Override
    public boolean delete(Article article) {

        String sql = "DELETE FROM ARTICLE Where id = ?;";

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PWD);
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, article.getId());

            // Execute the statement
            return stmt.executeUpdate() > 0;

        } catch (SQLException e) {
            // Handle the exception
            System.out.println("An error occurred: " + e.getMessage());
        }
        return false;
    }

    @Override
    public int updatePrix(String designation, Double promotion) {

        String sql = "UPDATE ARTICLE  SET PRIX = PRIX * ? Where DESIGNATION LIKE ?;";

        try (Connection conn = DriverManager.getConnection(DB_URL,DB_USER,DB_PWD);
             PreparedStatement stmt = conn.prepareStatement(sql);) {

            // Set the parameters
            stmt.setDouble(1, 1 - (promotion / 100));
            stmt.setString(2, "%" + designation + "%");
            // Execute the statement
            return stmt.executeUpdate();

        } catch (SQLException e) {
            // Handle the exception
            System.out.println("An error occurred: " + e.getMessage());
        }
        return 0;
    }

    @Override
    public double moyennePrix() {

        String sql = "SELECT AVG(PRIX) FROM ARTICLE;";

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PWD);
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()){
            while (rs.next()){
                return rs.getDouble(1);
            }

        } catch (SQLException e) {
            // Handle the exception
            System.out.println("An error occurred: " + e.getMessage());
        }

        return 0;
    }

    @Override
    public boolean deleteLike(String designation) {
        String sql = "DELETE FROM ARTICLE Where DESIGNATION like ?;";

        try (Connection conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PWD);
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, '%' + designation + '%');

            // Execute the statement
            return stmt.executeUpdate() > 0;

        } catch (SQLException e) {
            // Handle the exception
            System.out.println("An error occurred: " + e.getMessage());
        }
        return false;
    }
}
