package service;

import dto.UserDto;
import java.util.Optional;

import dao.LoginDao;
import dao.LoginDaoImpl;


public class LoginServiceImpl implements LoginService{
	private static LoginService instance = new LoginServiceImpl();
	private LoginDao loginDao = LoginDaoImpl.getInstance();
    public static LoginService getInstance() {
        return instance;
    }
	@Override
    public UserDto loginByEmail(String email) throws RuntimeException{
		UserDto userDto = loginDao.loginByEmail(email);
		
		return userDto;
	}
	
}
