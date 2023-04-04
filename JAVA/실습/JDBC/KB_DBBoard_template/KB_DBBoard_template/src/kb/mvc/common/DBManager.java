package kb.mvc.common;
/**
 * JDBC를 위한 로드, 연결, 닫기
 * */

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DBManager {

	/**
	 * 로드
	 * */
	static {
		try {
		  Class.forName(DBProperties.DRVIER_NAME);
		}catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 연결
	 * */
	
	public static Connection getConnection() throws SQLException{
		return DriverManager.getConnection(DBProperties.URL,
				DBProperties.USER_ID, DBProperties.USER_PASS);
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





