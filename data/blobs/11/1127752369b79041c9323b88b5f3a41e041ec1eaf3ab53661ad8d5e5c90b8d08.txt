package hibernate_test;

import hibernate_test.entity.Employee;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import java.util.List;

public class Test3 {
    public static void main(String[] args) {
        SessionFactory factory = new Configuration().configure("hibernate_test/hibernate.cfg.xml")
                .addAnnotatedClass(Employee.class)
                .buildSessionFactory();

        try {
            Session session = factory.getCurrentSession();
            session.beginTransaction();

//            List<Employee> employeeList = session.createQuery("from Employee")
//                            .getResultList();

            List<Employee> employeeList = session.createQuery("from Employee where  firstName = 'Mikhail' AND salary>650")
                    .getResultList();

            for (Employee employee : employeeList) {
                System.out.println(employee);
            }
            session.getTransaction().commit();

            System.out.println("Done");

        } finally {
            factory.close();
        }


    }
}
