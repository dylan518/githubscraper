package com.varxyz.jv250.jdbc.banking;

import java.sql.*;
import java.util.*;

public class AccountDao {
	private static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
	private static final String JDBC_URL = "jdbc:mysql://localhost:3306/jv250?serverTimezone=Asia/Seoul";
	private static final String JDBC_USER = "jv250";
	private static final String JDBC_PASSWORD = "jv250";

	public AccountDao() { // DB연결한다
		try {
			Class.forName(JDBC_DRIVER); // 드라이브를 연결한다 try catch 필수
			System.out.println("LOADED DRIVER ----> " + JDBC_DRIVER);

		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	/**
	 * 신규 계좌 등록
	 * 
	 * @param account
	 */

	public void addAccount(Account account) {
		String sql = "INSERT INTO Account(accountNum,balance,interestRate,overdraft,accountType,customerId) VALUES(?,?,?,?,?,?)";
		try {
			Connection con = null;
			PreparedStatement pstmt = null;

			try {
				con = DriverManager.getConnection(JDBC_URL, JDBC_USER, JDBC_PASSWORD);
				pstmt = con.prepareStatement(sql);
				pstmt.setString(1, account.getAccountNum());
				pstmt.setDouble(2, account.getBalance());

				if (account instanceof SavingsAccount) { // account가 saving 인지 checking인지 확인하는 if문
					SavingsAccount sa = (SavingsAccount) account;
					pstmt.setDouble(3, sa.getInterestRate());
					pstmt.setDouble(4, 0.0);
					pstmt.setString(5, String.valueOf('s'));

				} else {
					CheckingAccount ca = (CheckingAccount) account;
					pstmt.setDouble(3, 0.0);
					pstmt.setDouble(4, ca.getOverdraftAmount());
					pstmt.setString(5, String.valueOf("C"));
				}
				pstmt.setLong(6, account.getCustomer().getCid());
				pstmt.executeUpdate();
				System.out.println("INSERTED.....");
			} finally {
				pstmt.close();
				con.close();
			}
			System.out.println("NEW ACCOUNT INSERTED......\n");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * 전달된 주민번호를 가진 특정 고객의 계좌 목록 조회
	 */

	public List<Account> findAccountBySsn(String ssn) {
		String sql = "SELECT a.aid, a.accountNum, a.balance, a.interestRate, a.overdraft, a.accountType, c.name, c.ssn, c.phone, a.regDate"
				+ " FROM Account a INNER JOIN Customer c ON a.customerId = c.cid WHERE c.ssn = ?";
		List<Account> list = new ArrayList<>();
		try {
			Connection con = null;
			PreparedStatement pstmt = null;
			ResultSet rs = null;
			try {
				con = DriverManager.getConnection(JDBC_URL, JDBC_USER, JDBC_PASSWORD);
				pstmt = con.prepareStatement(sql);
				pstmt.setString(1, ssn);
				rs = pstmt.executeQuery();
				Account account = null;
				while (rs.next()) {
					if (rs.getString("accountType").charAt(0) == 's') {
						account = new SavingsAccount();
						((SavingsAccount) account).setInterestRate(rs.getDouble("interestRate"));
					} else {
						account = new CheckingAccount();
						((CheckingAccount) account).setOverdraftAmount(rs.getDouble("overdraft"));

					}
					account.setAid(rs.getLong("aid"));
					account.setAccoutNum(rs.getString("accountNum"));
					account.setBalance(rs.getDouble("balance"));
					account.setCustomer(new Customer(rs.getString("name"), rs.getString("ssn"), rs.getString("phone")));
					account.setRegDate(rs.getTimestamp("regDate"));

					list.add(account);
				}

			} finally {
				pstmt.close();
				con.close();
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

		return list;
	}

}
