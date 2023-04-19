package dao;

import java.sql.SQLException;
import java.util.Optional;

import dto.UserDto;
public interface LoginDao {
	UserDto loginByEmail(String email);
}
