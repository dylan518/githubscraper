package com.mvc.controller;

import java.io.IOException;
import java.util.Random;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class FindServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private int rNum;
	private int count = 0;  // 여기다 생성하는 이유는 밑에 생성하게 되면 count가 계속 0으로 초기화돼서 틀린 횟수를 맞출 수 가 없기 때문에 위에 privte로 선언.\
	public FindServlet() {
		Random r = new Random();
		rNum = r.nextInt(100) + 1;
		
	}
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		String uri = request.getRequestURI();
		int idx = uri.lastIndexOf("/");
		uri = uri.substring(idx + 1);
		String path = "/WEB-INF/views/";
		if ("find".equals(uri)) {		
			path += "find/find.jsp";
		}else if("check".equals(uri)) {			
			int num = Integer.parseInt(request.getParameter("num"));
			String msg = "맞춤"; // 
			if(num != rNum) {
				count++;
				msg = "틀렸다";
			}
			request.setAttribute("count", count); // request.setAttribute를 통해 result.jsp에 보내고 request.getAttriubte로 result.jsp에서 받아옴.
			request.setAttribute("msg", msg);
			path += "find/result.jsp";	
		}
		RequestDispatcher rd = request.getRequestDispatcher(path);
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		doGet(request, response);
	}

}
