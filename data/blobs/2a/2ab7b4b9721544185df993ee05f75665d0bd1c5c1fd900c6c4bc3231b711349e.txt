package board;

import java.sql.Date;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import board.model.BoardDAO;
import board.model.BoardDTO;
import common.Command;
import java.sql.Date;

public class InsertCommand implements Command {

	@Override
	public void exec(HttpServletRequest request, HttpServletResponse response) {
		// 비지니스로직
		// 화면에서 입력한 정보로 DB에 신규삽입저장하기
		
		BoardDTO dto = new BoardDTO();
		
		//subject, name, email, nalja, content, password
		dto.setSubject(request.getParameter("subject"));
		dto.setName(request.getParameter("name"));
		dto.setContent(request.getParameter("content"));
		dto.setEmail(request.getParameter("email"));
		dto.setPassword(request.getParameter("password"));
		dto.setNalja(Date.valueOf(request.getParameter("nalja")));
		
		new BoardDAO().registerBoard(dto);
	}

}
