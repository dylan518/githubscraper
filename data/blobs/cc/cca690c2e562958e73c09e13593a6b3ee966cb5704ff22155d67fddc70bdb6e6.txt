package com.pawansoft.util;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.hibernate.SessionFactory;
import org.hibernate.boot.Metadata;
import org.hibernate.boot.MetadataSources;
import org.hibernate.boot.registry.StandardServiceRegistry;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.cfg.Configuration;

public class HibernateUtil {


	private static final Logger log = LogManager.getLogger(HibernateUtil.class);
	private static SessionFactory sessionFactory;
	
	static {
		if(sessionFactory == null) {
			Properties props = new Properties(); 
			Configuration cfg = new Configuration();
			
			
			props = cfg.getProperties();
			log.info("JDBC URL: " + props.getProperty("hibernate.connection.url"));
			
			cfg.addAnnotatedClass(com.pawansoft.model.User.class);
			StandardServiceRegistry registry = new StandardServiceRegistryBuilder()
					.applySettings(cfg.getProperties())
					.build();
			
			Metadata metaData = new MetadataSources(registry)
					.getMetadataBuilder()
					.build();
			
			sessionFactory = metaData.getSessionFactoryBuilder().build();
			
			try {
				sessionFactory = cfg.buildSessionFactory();
			} catch (Exception e) {
				StandardServiceRegistryBuilder.destroy( registry );
				log.error("ERROR: ", e.getMessage());
			}
		}
	}
	
	public static SessionFactory getSessionFactory() {
		return sessionFactory;
	}
	
	public static Properties getAppProperties() {
		Properties r =  new Properties();
		InputStream input  = null;
		try {
			input = HibernateUtil.class.getClassLoader().getResourceAsStream("../resources/hibernate.cfg.xml");
			r.load(input);
			r.put("charSet", "UTF-8");
		} catch (NullPointerException npe) {
			log.error("tutorials.properties file not found.");
			//log.catching(npe);
		} catch (IOException e) {
			log.error(e);
			e.printStackTrace();
		} finally {
			if(input != null) {
				try {
					input.close();
				} catch (IOException ioe) {
					log.error(ioe.getMessage());
				}
			}
		}
		return r;
	}
}
