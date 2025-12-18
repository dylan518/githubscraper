import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ChooseBikesServlet")
public class ChooseBikesServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h2>Your Selected Bikes:</h2>");

        // Retrieve selected bikes from the request parameters
        String[] selectedBikes = request.getParameterValues("bike");
        if (selectedBikes != null && selectedBikes.length > 0) {
            out.println("<ul>");
            for (String bike : selectedBikes) {
                out.println("<li>" + bike + "</li>");
            }
            out.println("</ul>");
        } else {
            out.println("<p>No bikes selected.</p>");
        }
        out.println("</body></html>");
    }
}
