import dao.UserDao;
import dao.UserDaoImpl;
import dto.UserDto;

public class Test {

	public static void main(String[] args) {
		UserDao userDao = new UserDaoImpl();		
		
		
		// 등록
		//UserDto userDto = new UserDto(666, "육길동", "yook@gildong@com", "010-7777-7777", false);
//		int ret = userDao.insertUser(userDto);
//		System.out.println(ret);
//		// 테이블에서 등록 건을 확인한다.
		
		
		// 수정
//		userDto.setEmail("yook@gildong@com");
//		userDto.setPhone("010-7777-7777");
//		userDto.setSleep(true);
//		
//		int ret = userDao.updateUser(userDto);
//		System.out.println(ret);
		// 테이블에서 수정 건을 확인한다.
	
		// 전체 조회
//		List<UserDto> list = userDao.selectAll();
//		for (UserDto dto : list) {
//			System.out.println(dto);
//		}
//		// 테이블의 전체 조회 건과 비교 확인한다.

		
		// 1건 조회
//		UserDto dto = userDao.selectOne(666);
//		System.out.println(dto);
		// 테이블의 1건 조회 건과 비교 확인한다.
		

		// 삭제
		//int ret = userDao.deleteUser(userDto.getUserSeq());
		//System.out.println(ret);
		// 테이블에서 삭제 건을 확인한다.
	}

}
