package com.user.servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.omg.CORBA.Request;

import com.DAO.BooksDaoImpl;
import com.DAO.CratDaoImpl;
import com.DB.DBConnect;
import com.entity.Bookdetails;
import com.entity.Cart;

@WebServlet("/cartservlet")
public class CartServlet extends HttpServlet{

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		try {
			
			int bid=Integer.parseInt(req.getParameter("bid"));
			int uid=Integer.parseInt(req.getParameter("uid"));
			
			BooksDaoImpl dao = new BooksDaoImpl(DBConnect.getConn());
			Bookdetails b = dao.getBookById(bid);
			
			Cart c = new Cart();
			c.setBid(bid);
			c.setUid(uid);
			c.setBookname(b.getBookname());
			c.setAuthor(b.getAuthor());
			c.setPrice(b.getPrice());
			c.setTotalprice(b.getPrice());
			
			CratDaoImpl dao2=new CratDaoImpl(DBConnect.getConn());
			boolean f=dao2.addCart(c);
			
			HttpSession session=req.getSession();
			
			if(f) {
				session.setAttribute("addcart", "Book added to cart");
				resp.sendRedirect("allnewbooks.jsp");
			}else {
				session.setAttribute("failed", "Something went wrong on server");
				resp.sendRedirect("allnewbooks.jsp");
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	
	
	
}
