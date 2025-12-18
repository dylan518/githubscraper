package com.imnu.servlet;

import com.imnu.dao.coachdao;
import com.imnu.dao.dingdandao;
import com.imnu.dao.userdao;
import com.imnu.pojo.dingdanbean;
import com.imnu.pojo.userbean;
import com.imnu.util.getcookie;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

public class buycoach extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        int coachid = Integer.parseInt(request.getParameter("id"));
        String name = com.imnu.util.getcookie.getcookie("name",request);

        coachdao coachdao = new coachdao();
        String coachname = coachdao.selectonecoachnamebyid(coachid);

        userdao userdao = new userdao();
        userbean userbean = userdao.selectByName(name);
        int userid = userbean.getId();

        dingdandao dingdandao = new dingdandao();

        dingdanbean dingdanbean = new dingdanbean();

        dingdanbean.setUserid(userid);
        dingdanbean.setUsername(name);
        dingdanbean.setCoachid(coachid);
        dingdanbean.setCoachname(coachname);

        dingdandao.insertdingdan(dingdanbean);


        request.getRequestDispatcher("/searchCoach").forward(request,response);

    }
}
