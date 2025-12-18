import java.sql.*;  
import java.util.Scanner; 
//prepared statement 
class emp{
	int id;
	String name;
	int age;
	public void display(){
		System.out.println(id+" " + name + " "+age);
	}
	public void input(){
		Scanner in=new Scanner(System.in);
		System.out.println("Enter id: ");
		id=in.nextInt();
		System.out.println("Enter name: ");
		name=in.next();
		System.out.println("Enter age: ");
		age=in.nextInt();
	}
		

}
class OracleUpdate3{  
	public static void main(String[] args){  
		try{  
			//step1 load the driver class  
			Class.forName("oracle.jdbc.driver.OracleDriver");
			
			//step2 create  the connection object  
			Connection con=DriverManager.getConnection(  
				"jdbc:oracle:thin:@localhost:1521:xe","system","nitin");  
			 	
			//step3 create the statement object  
			String sql;
			sql = "create table emp(id number(10),name varchar2(40),age number(3))";
			PreparedStatement stmt=con.prepareStatement(sql);

			//step4 execute query  
			
			stmt.executeUpdate(sql);
			con.commit( );
			
			emp e1 = new emp();
			for( int i=0;i<3;i++){
				e1.input();
				String SQL = "INSERT INTO emp VALUES (?, ?, ?)";
				PreparedStatement pstmt = con.prepareStatement(SQL);
				pstmt.setInt(1, e1.id);// setter methods
				pstmt.setString(2, e1.name);
				pstmt.setInt(3, e1.age);
				pstmt.executeUpdate();
				pstmt.close();
			}
			stmt.executeUpdate("UPDATE emp " +
				"SET ID= " + 3 +
				"WHERE name = 'qwe'" );
			con.commit( );
			


			ResultSet rs=stmt.executeQuery("select * from emp");  
			while(rs.next()) {
				//System.out.println(rs.getInt(1)+"  "+rs.getString(2)+"  "+rs.getInt(3)); 
				e1.id=rs.getInt(1);
				e1.name=rs.getString(2);
				e1.age=rs.getInt(3);
				e1.display();
				
			}

			//step5 close the connection object  
			con.close();  
			stmt.close( );
  
		}
		catch(Exception e){
			System.out.println(e);
		}  
  
	}  
}