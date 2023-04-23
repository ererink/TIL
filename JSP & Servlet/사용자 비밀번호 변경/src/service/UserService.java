package service;

import dto.UserDto;

public interface UserService {
	int register(UserDto userDto);

	boolean changePwd(int userSeq, String currentPwd, String newPwd);
}
