

import jakarta.servlet.ServletException;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * Servlet implementation class Frutas
 */
@WebServlet("/Frutas")
public class Frutas extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter printWriter = response.getWriter();
		response.setContentType("text/html");
		
		String[] values = request.getParameterValues("frutas");
		printWriter.println("Frutas que você selecionou: ");
		
		for(int i=0; i<values.length; i++)
		{
			printWriter.println("<li>"+values[i]+"</li>");
		}
		
		printWriter.close();
	}

}
