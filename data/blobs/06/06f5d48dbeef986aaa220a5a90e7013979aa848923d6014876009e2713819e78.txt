package dao;
import java.sql.*;
import connectionManager.ConnectionManager;
import modal.product;

public class productDAO 
{	
public void addproduct(product p) throws ClassNotFoundException, SQLException 
{
	 int productId=p.getProductId();
	 String  productname=p.getProductname();
	 int msq=p.getMsq();
	 int price=p.getPrice();
	 int quantity=p.getQuantity();
	 ConnectionManager conm=new ConnectionManager();
	 Connection con=conm.establishConnection();
	 String query="insert into product values(?,?,?,?,?)";
	 PreparedStatement ps=con.prepareStatement(query);
	 ps.setInt(1,productId);
	 ps.setString(2,productname);
	 ps.setInt(3,msq);
	 ps.setInt(4,price);
	 ps.setInt(5,quantity);
	 ps.executeUpdate();
	 conm.closeConnection();
}
public void viewProduct() throws SQLException, ClassNotFoundException {
	ConnectionManager conm=new ConnectionManager();
	Connection con=conm.establishConnection();
	Statement st=con.createStatement();
	String q="Select * from product ";
	ResultSet rs=st.executeQuery(q);
	while(rs.next()) {
	      System.out.println(rs.getString("productName")+"||"+rs.getInt("productID")+"||"+rs.getInt("msq")+"||"+rs.getInt("price")+"||"+rs.getInt("quantity"));
		}
	
	conm.closeConnection();
}
public void update(product p) throws SQLException, ClassNotFoundException {
	ConnectionManager conm=new ConnectionManager();
	Connection con=conm.establishConnection();

	String q="Select * from product where productID =?";
	
	PreparedStatement ps1=con.prepareStatement(q);
	ps1.setInt(1, p.getProductId());
	ResultSet rs=ps1.executeQuery();
	
	
	if(rs.next()&&(rs.getInt("quantity")>p.getSoldquan())) {
	
		int newquan=rs.getInt("quantity")- p.getSoldquan();
		p.setQuantity(newquan);
		 String query="update product set quantity =? where productID=?";
         PreparedStatement ps=con.prepareStatement(query);
         ps.setInt(1,p.getQuantity());
         ps.setInt(2,p.getProductId());
         ps.executeUpdate();
		System.out.println("the remaining quantity "+rs.getInt("quantity"));
	}
	else {
		System.out.println("stock underflow or item not found");
	}
	conm.closeConnection();
}
public void delete(int id) throws ClassNotFoundException, SQLException {
	ConnectionManager conm=new ConnectionManager();
	Connection con=conm.establishConnection();

	String q="delete from product where productID =?";
	
	PreparedStatement ps1=con.prepareStatement(q);
	ps1.setInt(1, id);
	  ps1.execute();
	System.out.println("the product with the product id "+id+" is deteled");
	conm.closeConnection();
}

}
