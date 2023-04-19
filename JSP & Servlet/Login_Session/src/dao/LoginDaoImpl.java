package dao;
import common.DBManager;
import dto.UserDto;
import java.util.Optional;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class LoginDaoImpl implements LoginDao{
	private static LoginDao instance = new LoginDaoImpl();
	
	public static LoginDao getInstance() {
		return instance;
	}

	@Override
	public UserDto loginByEmail(String email) {
		Connection con = null;
        PreparedStatement ps = null;
        ResultSet rs = null;
        UserDto dto = null;
        String sql = "select * from chat where chat_id = ?";    	
        try{
        	con = DBManager.getConnection();
            ps = con.prepareStatement(sql);
            ps.setString(1, email);
            rs = ps.executeQuery();
            
            if (rs.next()){
                dto = new UserDto(
                		rs.getInt("userSeq"),
                        rs.getString("name"),
                        rs.getString("password"),
                        rs.getString("email"),
                        rs.getString("phone"),
                        Boolean.parseBoolean(rs.getString("is_sleep"))
                );
            }
            return dto;
        }catch(SQLException e){
			e.printStackTrace();

        }finally {
			DBManager.releaseConnection(con, ps, rs);
        }
		return null;
	}
	
	
}
