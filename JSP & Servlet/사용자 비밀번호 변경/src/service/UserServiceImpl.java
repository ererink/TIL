package service;

import dao.UserDao;
import dao.UserDaoImpl;
import dto.UserDto;

public class UserServiceImpl implements UserService{

	private static UserService instance = new UserServiceImpl();
	
	private UserDao userDao = UserDaoImpl.getInstance();
	
	private UserServiceImpl() {}
	
	public static UserService getInstance() {
		return instance;
	}
	
	@Override
	public int register(UserDto userDto) {
		return userDao.register(userDto);
	}
	
	@Override
	public boolean changePwd(int userSeq, String currentPwd, String newPwd) {
	    int result = userDao.checkPwd(userSeq, currentPwd);
	    if(result == 1) {
	        result = userDao.updatePwd(userSeq, newPwd);
	        if(result == 1) {
	            return true;
	        }
	    }
	    return false;
	}


}
