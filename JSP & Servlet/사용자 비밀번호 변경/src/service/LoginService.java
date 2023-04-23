package service;

import dto.UserDto;

public interface LoginService {
	public UserDto login(String email, String password);
}
