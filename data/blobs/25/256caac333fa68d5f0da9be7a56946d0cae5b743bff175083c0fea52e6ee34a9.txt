package br.com.kaiwang.gerenciador.servlet.controller;

import java.io.IOException;

import jakarta.servlet.Filter;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

public class AuthorizationFilter implements Filter {
	@Override
	public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain next) throws IOException, ServletException{
		HttpServletRequest request = (HttpServletRequest) servletRequest;
		HttpServletResponse response = (HttpServletResponse) servletResponse;
		
		String acction = request.getParameter("acction");
		
		HttpSession sessao = request.getSession();
		
		Boolean ProtectedRouter = !(acction.equals("logar") || acction.equals("formNovoUser"));
		Boolean UsuarioLogado = sessao.getAttribute("usuarioLogado") == null;
		
		if(ProtectedRouter && UsuarioLogado){
			response.sendRedirect("bem-vindo.jsp");
			return;
		}
		
		next.doFilter(request, response);
	}
}
