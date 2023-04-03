package jdbc.dao;


import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import jdbc.common.DBManager;
import jdbc.dto.UserDto;

public class UserDAOimpl implements UserDAO {

	@Override
	public int insert(UserDto userDto) {
		Connection con = null;
		PreparedStatement ps = null;
		int result = 0;
		String sql = "insert into users(user_seq, name, email, phone_number, is_sleep) values(?, ?, ?, ?, ?)";
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);

			ps.setInt(1, userDto.getUserSeq());
			ps.setString(2, userDto.getName());
			ps.setString(3, userDto.getEmail());
			ps.setString(4, userDto.getPhone());
			ps.setBoolean(5, userDto.isSleep());

			result = ps.executeUpdate();
		}catch (SQLException e){
			e.printStackTrace();
		}finally {
			DBManager.releaseConnection(con, ps);
		}
		return result;
	}

	@Override
	public int update(UserDto userDto) {
		Connection con = null;
		PreparedStatement ps = null;
		int result = 0;
		String sql = "update users set (user_seq, name, email, phone_number, is_sleep) = (?, ?, ?, ?, ?)";
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);

			ps.setInt(1, userDto.getUserSeq());
			ps.setString(2, userDto.getName());
			ps.setString(3, userDto.getEmail());
			ps.setString(4, userDto.getPhone());
			ps.setBoolean(5, userDto.isSleep());

			result = ps.executeUpdate();
		}catch (SQLException e){
			e.printStackTrace();
		}finally {
			DBManager.releaseConnection(con, ps);
		}
		return result;
	}

	@Override
	public List<UserDto> selectAll() {
		List<UserDto> list = new ArrayList<>();
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		String sql = "select user_seq, name, email, phone_number, is_sleep from users";
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);
			rs = ps.executeQuery();
			while (rs.next()){
				int user_seq = rs.getInt("user_seq");
				String name = rs.getString("name");
				String email = rs.getString("email");
				int phone_number = rs.getInt(4);
				String isSleep = rs.getString(5);
				list.add((UserDto) rs);
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}finally {
			DBManager.releaseConnection(con, ps, rs);
		}
		return list;
	}

	@Override
	public UserDto selectOne(int userSeq) {
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		String sql = "select user_seq from users where user_seq = ?";
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);
			rs = ps.executeQuery();
			UserDto ud = new UserDto();
			if (rs.next()){
				ud.setUserSeq(rs.getInt(1));
			}
			return ud;
		}catch (SQLException e) {
			e.printStackTrace();
		}finally {
			DBManager.releaseConnection(con, ps);
		}
		return null;
	}

	@Override
	public int delete(int userSeq) {
		Connection con = null;
		PreparedStatement ps = null;
		int result = 0;
		String sql = "delete from users where user_seq = ?";
		 try {
			 con = DBManager.getConnection();
			 ps = con.prepareStatement(sql);

			 ps.setInt(1, userSeq);

			 result = ps.executeUpdate();

		 }catch (SQLException e) {
			 e.printStackTrace();
		 }finally {
			 DBManager.releaseConnection(con, ps);
		 }
		return result;
	}

}
