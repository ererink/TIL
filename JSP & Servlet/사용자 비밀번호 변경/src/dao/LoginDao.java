package dao;

import dto.UserDto;

public interface LoginDao {
	public UserDto login(String email);
}
