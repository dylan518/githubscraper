package jdbc.dao.impl;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;

import config.ServerInfo;
import jdbc.dao.MemberDAO;
import jdbc.exception.DuplicateIDException;
import jdbc.exception.RecordNotFoundException;
import jdbc.vo.Member;

public class MemberDAOImpl implements MemberDAO{
	
	private static MemberDAOImpl dao = new MemberDAOImpl();
	private MemberDAOImpl() {
		
	}
	public static MemberDAOImpl getInstance() {
		return dao;
	}

	@Override
	public  Connection getConnect()throws SQLException {
		Connection conn = DriverManager.getConnection(ServerInfo.URL, 
										              ServerInfo.USER, 
										              ServerInfo.PASS);
		System.out.println("DB Connection....OK");
		return conn;
	}

	@Override
	public void closeAll(Connection conn, PreparedStatement ps)throws SQLException {
		if(ps!=null) ps.close();
		if(conn!=null) conn.close();
	}

	@Override
	public void closeAll(Connection conn, PreparedStatement ps, ResultSet rs)throws SQLException {
		if(rs!=null) rs.close();
		closeAll(conn, ps);		
	}
	
	private boolean isExist(int phone, Connection conn) throws SQLException{
		String query ="SELECT phone FROM member WHERE phone = ?";
		PreparedStatement ps = conn.prepareStatement(query);
		ps.setInt(1, phone);
		ResultSet rs = ps.executeQuery();
		return rs.next();
	}
	
	private boolean isExist(String email, Connection conn) throws SQLException{
		String query ="SELECT email FROM member WHERE email = ?";
		PreparedStatement ps = conn.prepareStatement(query);
		ps.setString(1, email);
		ResultSet rs = ps.executeQuery();
		return rs.next();
	}
	
	@Override
	public void insertMember(Member vo) throws SQLException, DuplicateIDException {
	    Connection conn = null;
        PreparedStatement ps = null;
        try {
           conn = getConnect();
           if(!isExist(vo.getPhone(), conn)) {
	           String query = "INSERT INTO member VALUES (seq_id.nextVal, ?, ?, ?)";
	           ps = conn.prepareStatement(query);
	           ps.setString(1, vo.getName());
	           ps.setString(2, vo.getEmail());
	           ps.setInt(3, vo.getPhone());
	           System.out.println(vo.getName()+" 고객 "+ps.executeUpdate()+"명이 가입 승인되었습니다");
           }else {
        	   throw new DuplicateIDException("이미 존재하는 휴대폰번호입니다");
           }
        }finally {
            closeAll(conn, ps);
        }
	}

	@Override
	public void deleteMember(int phone) throws SQLException, RecordNotFoundException {
		Connection conn = null;
        PreparedStatement ps = null;
        try {
           conn = getConnect();
           if(isExist(phone, conn)) {
        	   String query = "DELETE member WHERE phone = ?";
        	   ps = conn.prepareStatement(query);
        	   ps.setInt(1, phone);
        	   System.out.println(phone+" 휴대폰 번호를 가진 "+ps.executeUpdate()+"명의 고객이 삭제되었습니다");
           }else {
        	   throw new RecordNotFoundException("존재하지 않는 휴대폰번호 입니다");
           }
        }finally {
            closeAll(conn, ps);
        }	
	}

	@Override
	public void updateMember(Member vo) throws SQLException, RecordNotFoundException {
		Connection conn = null;
        PreparedStatement ps = null;
        try {
        	conn = getConnect();
            if(isExist(vo.getPhone(), conn)) {
         	   String query = "UPDATE member SET name = ?, email = ? WHERE phone = ?";
         	   ps = conn.prepareStatement(query);
         	   ps.setString(1, vo.getName());
         	   ps.setString(2, vo.getEmail());
         	   ps.setInt(3, vo.getPhone());
         	   System.out.println(vo.getPhone()+" 휴대폰 번호를 가진 "+ps.executeUpdate()+"명의 고객 정보가 변경되었습니다");
            }else {
         	   throw new RecordNotFoundException("존재하지 않는 휴대폰번호 입니다");
            }
        }finally {
            closeAll(conn, ps);
        }
	}

	@Override
	public Member getMember(int phone) throws SQLException, RecordNotFoundException {
		Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        Member member = null;
        try {
        	conn = getConnect();
            if(isExist(phone, conn)) {
         	   String query = "SELECT name, email, phone FROM member WHERE phone = ?";
         	   ps = conn.prepareStatement(query);
         	   ps.setInt(1, phone);
         	   rs = ps.executeQuery();
         	   if(rs.next()) {
         		  member = new Member(rs.getString("Name"), rs.getString("Email"), rs.getInt("phone"));
         	   }
            }else {
         	   throw new RecordNotFoundException("존재하지 않는 휴대폰번호 입니다");
            }
        }finally {
            closeAll(conn, ps,rs);
        }
		return member;
	}

	@Override
	public ArrayList<Member> getMember(String address) throws SQLException, RecordNotFoundException {
		Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        ArrayList<Member> members = new ArrayList<>();
        try {
        	conn = getConnect();
            if(isExist(address, conn)) {
         	   String query = "SELECT name, email, phone FROM member WHERE email = ?";
         	   ps = conn.prepareStatement(query);
         	   ps.setString(1, address);
         	   rs = ps.executeQuery();
         	   if(rs.next()) {
         		  members.add(new Member(rs.getString("Name"), rs.getString("Email"), rs.getInt("phone")));
         	   }
            }else {
         	   throw new RecordNotFoundException("존재하지 않는 이메일 입니다");
            }
        }finally {
            closeAll(conn, ps,rs);
        }
		return members;
	}

	@Override
	public ArrayList<Member> getMember() throws SQLException {
		Connection conn = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        ArrayList<Member> members = new ArrayList<>();
        try {
        	conn = getConnect();
        	String query = "SELECT name, email, phone FROM member";
      	   	ps = conn.prepareStatement(query);
	      	rs = ps.executeQuery();
	      	while(rs.next()) {
	      		  members.add(new Member(rs.getString("Name"), rs.getString("Email"), rs.getInt("phone")));
	      	}
        }finally {
            closeAll(conn, ps,rs);
        }
		return members;
	}

}
