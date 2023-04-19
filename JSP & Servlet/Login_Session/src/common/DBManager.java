package common;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class DBManager {
	private static DataSource datasource;
	
	/**
	 * 로드
	 * */
	static {
		try {
			Context context = (Context) new InitialContext().lookup("java:comp/env/");
			 datasource = (DataSource) context.lookup("jdbc/myoracle");
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 연결
	 * */
	
	public static Connection getConnection() throws SQLException{
		return  datasource.getConnection();
	}
	
	/**
	 * 닫기(DML전용)
	 * */
	public static void releaseConnection(Connection con, Statement st) {
		try {
			if(st!=null) st.close();
			if(con!=null)con.close();
		}catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	
	/**
	 * 닫기(select전용)
	 * */
    public static void releaseConnection(Connection con, Statement st, ResultSet rs) {
    	try {
    		if(rs!=null)rs.close();
    	}catch (SQLException e) {
			e.printStackTrace();
		}
    	releaseConnection(con, st);
	}
}
