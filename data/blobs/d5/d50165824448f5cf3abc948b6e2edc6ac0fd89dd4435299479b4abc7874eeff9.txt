package Student_Managment_System.dao;

import java.util.List;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.EntityTransaction;
import javax.persistence.Persistence;
import javax.persistence.Query;

import Student_Managment_System.dto.Student;

public class StudentDao {
	public EntityManager getEntityManager() {
		EntityManagerFactory entityManagerFactory=Persistence.createEntityManagerFactory("nanditha");
		EntityManager entityManager=entityManagerFactory.createEntityManager();
		return entityManager;
	}
	
	public Student saveStudent(Student student) {
		EntityManager entityManager=getEntityManager();
		EntityTransaction entityTransaction=entityManager.getTransaction();
		
		entityTransaction.begin();
		entityManager.persist(student);
		entityTransaction.commit();
		return student;
	}
	public Student loginStudent(String email) {
		EntityManager entityManager=getEntityManager();
		Query query=entityManager.createQuery("select s from Student s where s.email=?1");
		query.setParameter(1, email);
		Student student=(Student) query.getSingleResult();
		
		return student;
	}
	public Student updateStudent(Student student) {
		EntityManager entityManager=getEntityManager();
		EntityTransaction entityTransaction=entityManager.getTransaction();
		entityTransaction.begin();
		entityManager.merge(student);
		entityTransaction.commit();
		return student;
	}
	public boolean deleteStudent(int id) {
		EntityManager entityManager=getEntityManager();
		EntityTransaction entityTransaction=entityManager.getTransaction();
		Student student=entityManager.find(Student.class, id);
		if(student!=null) {
			entityTransaction.begin();
			entityManager.remove(student);
			entityTransaction.commit();
			return true;
		}
		else {
			return false;
		}
		
	}
	public Student getStudentById(int id) {
		EntityManager entityManager=getEntityManager();
		Student student=entityManager.find(Student.class, id);
		return student;
	}
	
	public List<Student> getAllStudent(){
		EntityManager entityManager=getEntityManager();
		Query query=entityManager.createQuery("select a from Student a");
		List<Student> list=query.getResultList();
		return list;
	}
}
