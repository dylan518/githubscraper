package com.demotest.util.dao.implementations;

import com.demotest.util.dao.interfaces.StudentDAO;
import com.demotest.entity.Student;
import jakarta.persistence.EntityManager;
import jakarta.persistence.TypedQuery;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * This is a `Repository class` which is made by adding the `@Repository` annotation before the class
 * This class is specialized component responsible for encapsulating storage, retrival and search behavior
 * related to data.
 * `@Transactional` is used to manage transactions which are sequences of operations that must be executed
 * as a single unit to maintain data integrity.
 * The translations have attributes such as propagation, isolation, timeout, rollbackFor.
 * `Propagation` is used if you want to set the transaction to run within a new transaction or within the current transaction.
 * `Isolation` is used to manage concurrency issues like dirty reads, non-repeatable reads and phantom reads.
 * `Timout` is used to set the time limit of the translation.
 * `Read-only` transactions can help optimize performance by avoiding unnecessary locks.
 * ` Rollback Rules` is used for when an unchecked exception is thrown.
 */

@Repository
public class StudentDAOImpl implements StudentDAO {

    private final EntityManager entityManager;

    @Autowired
    public StudentDAOImpl(EntityManager entityManager) {
        this.entityManager = entityManager;
    }

    @Transactional
    @Override
    public void save(Student student) {
        this.entityManager.persist(student);
    }

    @Override
    public Student findById(int id) {
        return this.entityManager.find(Student.class, id);
    }

    @Override
    public List<Student> findAll() {
        TypedQuery<Student> query = this.entityManager.createQuery("SELECT s FROM Student s ORDER BY s.lastName DESC", Student.class);
        return query.getResultList();
    }

    @Override
    public List<Student> findByFirstName(String lastName) {
        TypedQuery<Student> query = this.entityManager.createQuery("SELECT s FROM Student s WHERE s.firstName = :lastName", Student.class);
        query.setParameter("lastName", lastName);
        return query.getResultList();
    }

    @Transactional // This is put here because this changes the context of the db
    @Override
    public void update(Student student) {
        this.entityManager.merge(student);
    }

    @Transactional
    @Override
    public void delete(Integer id) {
        this.entityManager.remove(findById(id));
    }

    @Transactional
    @Override
    public int deleteAll() {
        return this.entityManager.createQuery("DELETE FROM Student").executeUpdate();
    }


}
