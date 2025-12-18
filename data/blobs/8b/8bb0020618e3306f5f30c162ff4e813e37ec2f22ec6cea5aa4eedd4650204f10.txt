package com.kl;

import java.util.Iterator;
import java.util.List;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import org.hibernate.query.Query;

public class RetriveSpec {

    public static void main(String[] args) {
        Configuration cfg = new Configuration();
        cfg.configure("hibernate.cfg.xml");
        
        SessionFactory sf = cfg.buildSessionFactory();
        Session s = sf.openSession();
        
        Transaction t = s.beginTransaction();
        
        Query<Employee> q = s.createQuery("from Employee", Employee.class);
        q.setFirstResult(1);
        q.setMaxResults(4);
        
        List<Employee> l = q.list();
        
        Iterator<Employee> i = l.iterator();
        while (i.hasNext()) {
            Employee e = i.next();
            System.out.println(e.getEname());
        }
        
        t.commit();
        s.close();
        sf.close();
    }
}