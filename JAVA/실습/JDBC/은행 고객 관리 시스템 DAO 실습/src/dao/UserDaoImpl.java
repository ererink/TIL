package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import common.DBManager;
import dto.UserDto;

// 아래 각 메소드를 구현하세요.
public class UserDaoImpl implements UserDao{
	private static UserDao instance = new UserDaoImpl();
	private UserDaoImpl(){}
	public static UserDao getInstance(){
		return instance;
	}
	@Override
	public int insertUser(UserDto userDto) throws RuntimeException{
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
			String isSleep = userDto.isSleep() ? "Y": "N";
			ps.setString(5, isSleep);
			result = ps.executeUpdate();

		}catch (SQLException e){
			e.printStackTrace();
			throw new RuntimeException("등록에 예외가 발생했습니다.");

		}finally {
			DBManager.releaseConnection(con, ps);
		}
		return result;
	}

	@Override
	public int updateUser(UserDto userDto) throws RuntimeException {
		Connection con = null;
		PreparedStatement ps = null;
		int result = 0;
		String sql = "update users set (name, email, phone_number, is_sleep) = (?, ?, ?, ?)";
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);

			ps.setString(1, userDto.getName());
			ps.setString(2, userDto.getEmail());
			ps.setString(3, userDto.getPhone());
			String isSleep = userDto.isSleep() ? "Y": "N";
			ps.setString(4, isSleep);

			result = ps.executeUpdate();

		}catch (SQLException e){
			e.printStackTrace();
			throw new RuntimeException("수정에 예외가 발생했습니다.");
		}finally {
			DBManager.releaseConnection(con, ps);
		}
		return result;
	}

	@Override
	public int deleteUser(int userSeq) {
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
			throw new RuntimeException("삭제에 예외가 발생했습니다.");

		}finally {
			DBManager.releaseConnection(con, ps);
		}
		return result;
	}

	@Override
	public List<UserDto> selectAll() throws RuntimeException{
		List<UserDto> list = new ArrayList<>();
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		String sql = "select user_seq, name, email, phone_number, is_sleep from users order by user_seq";
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);
			rs = ps.executeQuery();

			while (rs.next()){
				UserDto dto = new UserDto();
					dto.setUserSeq(rs.getInt("user_seq"));
					dto.setName(rs.getString("name"));
					dto.setEmail(rs.getString("email"));
					dto.setPhone(rs.getString("phone_number"));
					dto.setSleep(Boolean.parseBoolean(rs.getString("is_sleep")));

				list.add(dto);
			}
		} catch (SQLException e) {
			e.printStackTrace();
			throw new RuntimeException("전체 조회에 예외가 발생했습니다.");

		}finally {
			DBManager.releaseConnection(con, ps, rs);
		}
		return list;
	}

	@Override
	public UserDto selectOne(int userSeq) throws RuntimeException{
		Connection con = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		UserDto dto = null;
		String sql = "select user_seq, name, email, phone_number, is_sleep from users where user_seq = ?";
		try {
			con = DBManager.getConnection();
			ps = con.prepareStatement(sql);
			ps.setInt(1, userSeq);
			rs = ps.executeQuery();

			if (rs.next()){
				dto = new UserDto();
				dto.setUserSeq(rs.getInt("user_seq"));
				dto.setName(rs.getString("name"));
				dto.setEmail(rs.getString("email"));
				dto.setPhone(rs.getString("phone_number"));
				dto.setSleep(Boolean.parseBoolean(rs.getString("is_sleep")));
			}
			
		}catch (SQLException e) {
			e.printStackTrace();
			throw new RuntimeException("1건 조회에 예외가 발생했습니다.");

		}finally {
			DBManager.releaseConnection(con, ps, rs);
		}
		return dto;
	}

}
