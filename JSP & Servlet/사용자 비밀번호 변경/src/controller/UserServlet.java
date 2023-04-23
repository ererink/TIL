package controller;

import java.io.IOException;

import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dto.UserDto;
import service.UserService;
import service.UserServiceImpl;

/**
 * Servlet implementation class UserServlet
 */
@WebServlet("/user")
public class UserServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//가입
		String job = request.getParameter("job");
		switch(job) {
		   case "register" : register(request,response); break;
		   
		}
	}
	
	/**
	 * 가입하기
	 * */
	public void register(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		 //폼으로 전송된 데이터 받기
		String name = request.getParameter("name");
		String email = request.getParameter("email");
		String phone = request.getParameter("phone");
		String password = request.getParameter("password");
		
		//하나의 DTO객체로 만든다.
		UserDto dto = new UserDto(0, name, password, email, phone, false);
		System.out.println("dto = " + dto);
		
		UserService service = UserServiceImpl.getInstance();
		int result = service.register(dto);
		
		response.getWriter().print(result);
	}
	
	/**
	 * 비밀번호 변경
	 */
	public void changePwd(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	    HttpSession session = request.getSession();
	    
	    // 세션에서 로그인한 사용자의 정보 가져오기 
	    UserDto user = (UserDto) session.getAttribute("loginUser");
	    
	    // 변경하고자 하는 사용자의 userSeq를 가져오기 
	    int userSeq = user.getUserSeq();
	    
	    // 현재 비밀번호와 새로운 비밀번호를 파라미터로 받아오기 
	    String currentPwd = request.getParameter("currentPwd");
	    String newPwd = request.getParameter("newPwd");
	    
	    // changePwd 메소드를 호출하여 비밀번호를 변경한다.
	    UserService service = UserServiceImpl.getInstance();
	    boolean result = service.changePwd(userSeq, currentPwd, newPwd);

	    PrintWriter out = response.getWriter();
	    out.print(result);
	}


}





