package dao;

import dto.UserDto;

public interface UserDao {
	int register(UserDto userDto);
	
	int checkPwd(int userSeq, String password);
	
	int updatePwd(int userSeq, String password);
}
