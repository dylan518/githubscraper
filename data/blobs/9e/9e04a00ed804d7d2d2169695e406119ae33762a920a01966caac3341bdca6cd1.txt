package com.example.lesson23_24.servlets;

import com.example.lesson23_24.models.UserModel;
import com.example.lesson23_24.utils.ErrorUtil;
import com.example.lesson23_24.utils.UserUtil;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@WebServlet(name = "registration", urlPatterns = "/registration")
public class RegistrationServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        request.getRequestDispatcher("Registration.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        Map<String, String> candidateUserInfo = new HashMap<>();
        boolean isValidFields = validateFormFields(candidateUserInfo);

        candidateUserInfo.put("email", request.getParameter("email"));
        candidateUserInfo.put("name", request.getParameter("name"));
        candidateUserInfo.put("role", request.getParameter("role"));
        candidateUserInfo.put("password", request.getParameter("password"));

        if (!isValidFields) {
            ErrorUtil.generateIncorrectRegistrationFields(response);
        } else {
            List<UserModel> users = (List<UserModel>)request.getServletContext().getAttribute("users");
            boolean isCorrectRegistration = UserUtil.registrateUser(candidateUserInfo, users);

            if (isCorrectRegistration) {
                response.sendRedirect("/login");
            } else {
                ErrorUtil.generateIncorrectRegistrationFields(response);
            }
        }
    }

    private boolean validateFormFields(Map<String, String> candidateUserInfo) {
        Collection<String> values = candidateUserInfo.values();
        boolean isValidFields = true;

        for (String value : values) {
            if (value == null || value.isEmpty()) {
                isValidFields = false;
            }
        }

        return isValidFields;
    }
}
