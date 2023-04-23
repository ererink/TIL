package service;

import dao.LoginDao;
import dao.LoginDaoImpl;
import dto.UserDto;

public class LoginServiceImpl implements LoginService{
	private LoginDao loginDao = new LoginDaoImpl();
	@Override
	public UserDto login(String email, String password) {
		
		
		UserDto userDto = loginDao.login(email);
		System.out.println("email = "+email);
		System.out.println("password = " + password);
		System.out.println(userDto);
		if( userDto != null && userDto.getPassword().equals(password)) {
			userDto.setPassword(null); // password null 처리
			return userDto;
		}else {
			return null;
		}
	}
}

