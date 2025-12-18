package example.utilities;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import example.entity.Movie;

public class HibernateUtil 
{
	public static SessionFactory buildSessionFactory()
	{
		Configuration conf = new Configuration().configure();
		Class<Movie> movieType = Movie.class;
		conf.addAnnotatedClass(movieType);
		SessionFactory sf = conf.buildSessionFactory();
		return sf;
	}
}
