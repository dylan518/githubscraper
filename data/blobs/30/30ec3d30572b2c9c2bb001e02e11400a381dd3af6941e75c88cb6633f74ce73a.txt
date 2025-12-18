package edu.kh.TodoList.controller;

import java.io.IOException;

import edu.kh.TodoList.service.TodoListServiceImpl;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@WebServlet("/todo/add")
public class TodoAddServlet extends HttpServlet{
		
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		try {
			
			TodoListServiceImpl service = new TodoListServiceImpl();
			String title = req.getParameter("title");
			String detail = req.getParameter("detail");
			
			int index = service.todoAdd(title, detail);
			
			String message = null;
			if(index > -1) message ="추가 성공";
			else message = "추가 실패";

			
			HttpSession session = req.getSession();
			session.setAttribute(message, session);
			
			resp.sendRedirect("/");
			
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
}
