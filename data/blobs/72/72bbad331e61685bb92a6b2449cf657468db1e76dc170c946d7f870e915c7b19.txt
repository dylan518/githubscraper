package com.cyb.json;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

/**
 * Servlet implementation class JsonServlet2
 */
@WebServlet("/json2")
public class JsonServlet2 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public JsonServlet2() {
        super();
   
    }
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doHandle(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doHandle(request, response);
	}
	protected void doHandle(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html; charset=utf-8");
		
		PrintWriter out = response.getWriter();
		
		JSONObject jsonObject = new JSONObject();	//	"members"
		JSONArray membersArray = new JSONArray();	// []
		JSONObject memberObject = new JSONObject();	//	{"name":"홍"~~}	
	
		// 한 사람의 정보
		memberObject.put("name","홍길동");
		memberObject.put("age","58");
		memberObject.put("gender","남자");
		memberObject.put("nickname","대도");
		
		// 한 사람의 정보를 배열에 추가
		membersArray.add(memberObject);
		memberObject = new JSONObject();
		
		memberObject.put("name","홍길순");
		memberObject.put("age","13");
		memberObject.put("gender","여자");
		memberObject.put("nickname","순이");
		
		// 두 번째 사람의 정보를 배열에 추가
		membersArray.add(memberObject);
		
		jsonObject.put("members", membersArray);
		
		// 여기까지는 JSON 객체에 데이터 추가 부분
		
		// 아래부터는 JSON 객체를 문자열로 변환하여 응답 처리.
		String jsonInfo = jsonObject.toJSONString();
		
		System.out.println(jsonInfo);
		out.print(jsonInfo);	// 문자열로 응답 처리!
	}

}
