package com.xwork.newyear.reposistoery;

import com.xwork.newyear.entity.UserEntity;
import org.jboss.logging.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Query;
import javax.persistence.TypedQuery;
import javax.transaction.Transactional;
import java.util.List;

@Repository
public class UserReposistoeryImpl implements UserReposisteory {

    @Autowired
    EntityManagerFactory factory;

    @Override
    public boolean Save(UserEntity userEntity) {

        EntityManager entityManager = factory.createEntityManager();
        entityManager.getTransaction().begin();
        entityManager.persist(userEntity);
        entityManager.getTransaction().commit();
        entityManager.close();
        return true;
    }

    @Override
    public UserEntity findByEmail(String email) {
        EntityManager entityManager = factory.createEntityManager();
        TypedQuery<UserEntity> query = entityManager.createNamedQuery("UserEntity.findByEmail", UserEntity.class);
        query.setParameter("email", email);
        List<UserEntity> results = query.getResultList();
        entityManager.close();
        if (results.isEmpty()) {
            return null;
        }
        return results.get(0);

    }


    @Override
    public boolean updatePassword( String email, String password, String confirmPwd) {
        EntityManager entityManager = factory.createEntityManager();
        entityManager.getTransaction().begin();
         entityManager.createNamedQuery("updatePassword")
                .setParameter("password", password)
                .setParameter("confirmPwd", confirmPwd)
                .setParameter("email", email).executeUpdate();
         entityManager.getTransaction().commit();
         entityManager.close();
         return true;
    }


}

