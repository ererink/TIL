package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import common.DBManager;
import dto.UserDto;

public class LoginDaoImpl implements LoginDao {
	
	@Override
	public UserDto login(String email) {
		
		UserDto userDto = null;
		Connection con = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		try {
			con = DBManager.getConnection();
			String sql = 
					"select user_seq, name, password, email, phone, is_sleep  " + 
					"  from users where email = ? ";
			pstmt = con.prepareStatement(sql);
			pstmt.setString(1,  email);
			
			System.out.println(email);
			rs = pstmt.executeQuery();

			if(rs.next()) {
				userDto = new UserDto();
				userDto.setUserSeq(rs.getInt("user_seq"));
				userDto.setName(rs.getString("name"));
				userDto.setPassword(rs.getString("password"));
				userDto.setEmail(rs.getString("email"));
				userDto.setPhone(rs.getString("phone"));
				userDto.setSleep(( "Y".equals(rs.getString("is_sleep"))));
			}
			
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			DBManager.releaseConnection(con, pstmt, rs);
		}
		
		return userDto;
	}

}
