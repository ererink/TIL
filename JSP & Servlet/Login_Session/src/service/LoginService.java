package service;

import java.util.Optional;

import dto.UserDto;

public interface LoginService {
	UserDto loginByEmail(String email);

}
