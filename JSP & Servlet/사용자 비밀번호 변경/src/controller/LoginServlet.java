package controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import dto.UserDto;
import service.LoginService;
import service.LoginServiceImpl;

/**
 * Servlet implementation class LoginServlet
 */
@WebServlet(urlPatterns = { "/login", "/logout" } , loadOnStartup = 1)
public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	/**
	 *  로그인
	 * */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String email = request.getParameter("email");
		String pass = request.getParameter("pass");
		System.out.println("email = " + email);
		System.out.println("pass = " + pass);
		
		LoginService service = new LoginServiceImpl();
		UserDto dto = service.login(email, pass);
		
		String result="fail";
		if(dto!=null) {
			result="success";
			//로그인성공이니  session에 사용자의 정보를 저장
			HttpSession session = request.getSession();
			session.setAttribute("userDto", dto);//뷰에서 ${sessionScope.userDto}가능
			 
		}
		
		Gson gson = new Gson();
		JsonObject obj =new JsonObject();
		obj.addProperty("result", result);
		
		String jsonArr = gson.toJson(obj);
		System.out.println("jsonArr = " + jsonArr);
		
		PrintWriter out =response.getWriter();
		out.print(jsonArr);
		
	}//doPostEnd
	
	
   /**
    * 로그아웃
    * */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//모든세션의정보를 정리=삭제
		 request.getSession().invalidate();//모든세션정보제거
		 response.sendRedirect("index.jsp");
		
	}

	

}


