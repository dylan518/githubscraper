package application;

import domain.Person;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class Main {

    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("maven-jpa");
        EntityManager em = emf.createEntityManager();

        Person p = em.find(Person.class, 2);

        em.getTransaction().begin();

        em.remove(p);

        em.getTransaction().commit();

        System.out.println("Done!");

        em.close();
        emf.close();
    }
}