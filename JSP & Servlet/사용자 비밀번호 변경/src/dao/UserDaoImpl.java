package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import common.DBManager;
import dto.UserDto;

public class UserDaoImpl implements UserDao{

	private static UserDao instance = new UserDaoImpl();
	
	private UserDaoImpl() {}
	
	public static UserDao getInstance() {
		return instance;
	}
	
	@Override
	public int register(UserDto userDto) {
		String sql = "insert into users (user_seq, name, email, phone, password) values (user_seq.nextval, ?, ?, ?, ?) ";
		Connection con = null;
		PreparedStatement pstmt = null;
		int ret = 0;
		try {
			con = DBManager.getConnection();
			pstmt = con.prepareStatement(sql);
			
			pstmt.setString(1, userDto.getName());
			pstmt.setString(2, userDto.getEmail());
			pstmt.setString(3, userDto.getPhone());
			pstmt.setString(4, userDto.getPassword());
			
			ret = pstmt.executeUpdate();
			
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			DBManager.releaseConnection(con, pstmt);
		}
		
		return ret;
	}
	
	public int checkPwd(int userSeq, String password) {
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		int result = 0;
		String sql = "select password from users where user_seq = ?";
		
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);
			ps.setInt(1, userSeq);
			rs = ps.executeQuery();

			if(rs.next()) {
				String chkPw = rs.getString("password");
				if(password.equals(chkPw)) {
					result = 1;
				}		
				
			}
		}catch (SQLException e) {
			e.printStackTrace();
			throw new RuntimeException("비밀번호 확인에 예외가 발생했습니다.");

		}finally {
			DBManager.releaseConnection(con, ps, rs);
		}
		return result;
	}
	
	public int updatePwd(int userSeq, String password) {
		Connection con = null;
		PreparedStatement ps = null;
		int result = 0;
		String sql = "update users set password = ? where user_seq = ?";
		
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);

			ps.setString(1, password);
			ps.setInt(2, userSeq);		

			result = ps.executeUpdate();

		}catch(Exception e) {
			e.printStackTrace();
			throw new RuntimeException("비밀번호 변경에 예외가 발생했습니다.");

		}finally {
			DBManager.releaseConnection(con, ps);
		}

		return result;
		
	}

}
