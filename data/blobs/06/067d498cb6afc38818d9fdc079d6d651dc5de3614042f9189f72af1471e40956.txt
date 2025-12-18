package market.controller;

import java.io.IOException;
import java.sql.Connection;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import market.dao.BoardDAO;
import market.vo.BoardVO;

@WebServlet("*.do")
public class BoardController extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private HttpSession session;
	private BoardDAO bdao;
	private String url;
	
	public void init(ServletConfig config) throws ServletException {
		// ServletContext의 con 속성에서 connection 객체를 받아와서 bdao 객체 생성
		bdao = new BoardDAO();
		bdao.setCon((Connection) config.getServletContext().getAttribute("con"));
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doPost(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String cmd = request.getRequestURI().substring(request.getContextPath().length());
		session = request.getSession();
		boolean sendFlag = false;
		System.out.println("cmd : " + cmd);
		switch (cmd) {
		case "/BoardList.do":
			list(request);
			break;
		case "/BoardWriteForm.do":
			url = "/board/boardWrite.jsp";
			break;
		case "/BoardWrite.do":
			write(request);
			sendFlag = true;
			break;
		case "/BoardModify.do":
			modify(request);
			sendFlag = true;
			break;
		case "/BoardRemove.do":
			remove(request);
			sendFlag = true;
			break;
		case "/BoardView.do":
			view(request);
			break;
		case "/BoardSearchSubject.do":
			search(request, "subject");
			break;
		case "/BoardSearchContent.do":
			search(request, "content");
			break;
		case "/BoardSearchUserid.do":
			search(request, "Userid");
			break;

		default:
			break;
		}
		//cmd가 	/BoardList.do 면 게시판 목록 조회
		//		/BoardWriteForm.do 면 게시물 작성 폼으로 이동
		//		/BoardWrite.do 면 게시물 작성 처리
		// ...
		System.out.println("url : " + url);
		if(!sendFlag) {
			RequestDispatcher rd = request.getRequestDispatcher(url);
			rd.forward(request, response); // 저장된 url로 포워딩
		} else {
			response.sendRedirect(url);
		}
	}
	
	public void view(HttpServletRequest req) { // 게시물 조회
		// 파라미터로 전달된 게시물 번호를 받아서 게시물 조회
		int num = Integer.parseInt(req.getParameter("num"));
		BoardVO bvo = bdao.select(num);
		// 자신이 작성한 게시물의 조회수는 올리지 않음
		updateHit(bvo);
		// 해당 게시물을 요청 객체의 bvo 속성에 저장한 후 이동 url을 게시판 조회 페이지로 설정
		req.setAttribute("bvo", bvo);
		url = "/board/boardView.jsp";
	}
	
	public void modify(HttpServletRequest req) { // 게시물 조회
		// 파라미터로 전달된 게시물 번호, 제목 내용을 받아서 BoardVO에 저장
		BoardVO bvo = new BoardVO();
		bvo.setNum(Integer.parseInt(req.getParameter("num")));
		bvo.setSubject(req.getParameter("subject"));
		bvo.setContent(req.getParameter("content"));
		// 게시물 수정 처리를 한 후 수정에 성공하면 세션의 msg 속성에 '게시물이 수정되었습니다.'를 저장하고
		if(bdao.update(bvo)) {
			session.setAttribute("msg", "게시물이 수정되었습니다.");
		} else {
			session.setAttribute("msg", "게시물 수정에 실패하였습니다.");
		}
		// 실패하면 '게시물 수정에 실패하였습니다.' 저장 후
		// boardList 지정
		url = "/market/BoardList.do";
	}
	
	public void remove(HttpServletRequest req) { // 게시물 조회
		//System.out.println(req.getParameter("num"));
		if(bdao.delete(req.getParameter("num"))) {
			session.setAttribute("msg", "게시물이 삭제되었습니다.");
		} else {
			session.setAttribute("msg", "게시물 삭제에 실패하였습니다.");
		}
		// 게시물 수정 처리를 한 후 수정에 성공하면 세션의 msg 속성에 '게시물이 삭제되었습니다.'를 저장하고
		// 실패하면 '게시물 삭제에 실패하였습니다.' 저장 후
		// boardList 지정
		url = "/market/BoardList.do";
	}
	
	public void list(HttpServletRequest req) { // 게시판 목록 조회
		// 게시판 목록을 요청 객체의 boardList속성에 저장\
		List<BoardVO> list = bdao.selectAllContent();
		req.setAttribute("boardList", list);
		// 전체 게시물 수를 요청 객체의 total 속성에 저장
		req.setAttribute("total", bdao.totalCount());
		// 이동 url을 게시판 목록 페이지로 지정
		url = "/board/boardList.jsp";
	}
	
	public void write(HttpServletRequest req) { // 게시판 작성
		// 요청 파라미터로 전달된 게시물 제목, 내용, 작성자, ip(getRemoteAddr())를 BoardVO 에 저장
		BoardVO bvo = new BoardVO();
		bvo.setUserid(req.getParameter("userid"));
		bvo.setSubject(req.getParameter("subject"));
		bvo.setContent(req.getParameter("content"));
		bvo.setIp(req.getRemoteAddr());
		// 게시물 등록 처리를 한 후 등록에 성공하면
		if(bdao.insert(bvo)) {
			// 세션의 msg 속성에 '게시물이 등록되었습니다.' 를 저장한 후 이동 url을 게시판 목록 페이지로 지정
			session.setAttribute("msg", "게시물이 등록되었습니다.");
			url = "/market/BoardList.do";
		}
		
	}
	
	public void search(HttpServletRequest req, String where) { // 게시판 작성

		List<BoardVO> list = bdao.search(where, req.getParameter("searchText"));
		System.out.println(list.size());
		req.setAttribute("boardList", list);
		req.setAttribute("total", bdao.totalCount());
		url = "/board/boardList.jsp?search="+req.getParameter("searchText")+"&select="+req.getParameter("select");
	}
	
	public void updateHit(BoardVO bvo) { // 게시물 조회수 증가
		if(bvo != null) {
			if (!bvo.getUserid().equals(session.getAttribute("sid"))) {
				if ( bdao.updateHit(bvo.getNum(), bvo.getHit()+1) ) {
					bvo.setHit(bvo.getHit()+1);
				} else {
					System.out.println("setHit Fail");
				}
			}
		}
	}
}
