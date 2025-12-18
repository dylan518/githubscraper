package com.bank.Servlets;

import java.io.IOException;

import com.bank.DAO.CustomerDAOImpl;
import com.bank.DAO.CustomerDAOInterface;
import com.bank.DTO.Customer;

import jakarta.servlet.RequestDispatcher;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@WebServlet("/ForgotPin")
public class ForgotPin extends HttpServlet{
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		HttpSession session=req.getSession(false);
		Customer c=(Customer)session.getAttribute("customer");
		int oldPin=c.getPin();
		CustomerDAOInterface cdao=new CustomerDAOImpl();
		long accNum=Long.parseLong(req.getParameter("accountNumber"));
		c.setAccno(accNum);
		long phone=Long.parseLong(req.getParameter("phoneNumber"));
		c.setPhone(phone);
		int pin=Integer.parseInt(req.getParameter("newPin"));
		int confirmPin=Integer.parseInt(req.getParameter("confirmNewPin"));
		
		if(oldPin!=pin) {
		if(pin==confirmPin) {
			c.setPin(pin);
			boolean res=cdao.updateCustomer(c);
			if(res) {
				session.setAttribute("pinsuccess", "Pin Changed successfully");
				RequestDispatcher rd=req.getRequestDispatcher("ForgotPin.jsp");
				rd.forward(req, resp);
			}
			else {
				session.setAttribute("pinfailure", "Pin Change failure");
				RequestDispatcher rd=req.getRequestDispatcher("ForgotPin.jsp");
				rd.forward(req, resp);
			}
		}
		else {
			session.setAttribute("pinfailure", "Pin and confirm pin doesn't match");
			RequestDispatcher rd=req.getRequestDispatcher("ForgotPin.jsp");
			rd.forward(req, resp);
		}
		}
		else {
			session.setAttribute("pinfailure", "Your old pin and new can cannot be same");
			RequestDispatcher rd=req.getRequestDispatcher("ForgotPin.jsp");
			rd.forward(req, resp);
		}
	}
}

