package in.co.rays.basic;

import java.sql.Date;
import java.text.SimpleDateFormat;

public class Testdate {

	public static void main(String[] args) {
		
		Date d=new Date(0);
		
		System.out.println(d);
		
		SimpleDateFormat sdf = new SimpleDateFormat("dd/mm/yyyy");
				
				String s=sdf.format(d);
		System.out.println(s);
	}

}
