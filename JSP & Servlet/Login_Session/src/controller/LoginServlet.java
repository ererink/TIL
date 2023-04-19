package controller;

import java.io.IOException;

//import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import dto.UserDto;
import service.LoginService;
import service.LoginServiceImpl;

/**
 * Servlet implementation class LoginServlet
 */
@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
//       
//    String dbEmail, dbPwd;
//    
// // 서블릿에 대한 환경설정 정보를 담고있다.
// 	@Override
// 	public void init(ServletConfig config) throws ServletException {
// 		dbEmail = config.getInitParameter("email");
// 		dbPwd = config.getInitParameter("pwd");
// 	}
 	
 	public LoginServlet() {
 		
 	}
	/**
	 * 로그아웃
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		HttpSession session = request.getSession();
		session.invalidate();
	}

	/**
	 * 로그인
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
		
		LoginService loginService = LoginServiceImpl.getInstance();
		
		request.setCharacterEncoding("UTF-8");
		
		String userEmail = request.getParameter("userEmail");
		String userPwd = request.getParameter("userPwd");
		//String userName = request.getParameter("userName");
		
		UserDto user = loginService.loginByEmail(userEmail); 
		
		
		if(user.getEmail().equals(userEmail) && user.getPassword().equals(userPwd)) {
						
			// 저장
			request.setAttribute("user", user); // request가 유지되는 동안
			
			request.getRequestDispatcher("LoginServiceImpl.java").forward(request, response);
			
			
		}else {
			response.setContentType("text/html;charset=UTF-8");

			request.setAttribute("errMsg", "로그인 정보를 확인해주세요");
			//request.getRequestDispatcher("/error.jsp").forward(request, response);

		}
	}

}


