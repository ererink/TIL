package servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(
		urlPatterns = {"/post"}, 
		loadOnStartup = 1

)
public class ParameterServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	// test by browser address with query string 
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		// 서버에서 읽는 경우는 GET 방식에서는 없어도 된다. 하지마, 항상 해 주도록 향후에는 Filter 등으로 처리
		// 브라우저에 보내는 경우는 한글 처리 필요.
		
		request.setCharacterEncoding("utf-8"); 
		response.setContentType("text/html; charset=utf-8");
		
		// 파라미터 처리하기
		String job = request.getParameter("job");	
		String pageNo = request.getParameter("pageNo");		
		String searchWord = request.getParameter("searchWord");
		
		// 서버 출력
		System.out.println("job : " + job);
		System.out.println("pageNo : " + pageNo);
		System.out.println("searchWord : " + searchWord);
		
		// 브라우저에 보내기
		// use StringBuilder
		StringBuilder sb = new StringBuilder();
		sb.append("<h1>job : ").append(job).append("</h1>");
		sb.append("<h1>pageNo : ").append(pageNo).append("</h1>");
		sb.append("<h1>searchWord : ").append(searchWord).append("</h1>");
				
		response.getWriter().append(sb);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		request.setCharacterEncoding("utf-8"); // need with POST
		response.setContentType("text/html; charset=utf-8");
		
		// 파라미터 처리하기
		String name = request.getParameter("name");
		String email = request.getParameter("email");
		String gender = request.getParameter("gender");
		
		String hobby[] = request.getParameterValues("hobby");
		StringBuilder sbHobby = new StringBuilder();
		for (String h : hobby) {
			sbHobby.append(h).append(", ");
		}
		sbHobby.setLength(sbHobby.length()-2);
		
		String favorite = request.getParameter("favorite");
		String desc = request.getParameter("desc");
		
		// ParameterDto 객체 생성
	    ParameterDto dto = new ParameterDto(name, email, gender, hobby, favorite, desc);
	    
	    request.setAttribute("dto", dto);
	    
	    RequestDispatcher dispatcher = request.getRequestDispatcher("postResult.jsp");
	    dispatcher.forward(request, response);

		// 서버 출력
		System.out.println("name : " + name);
		System.out.println("email : " + email);
		System.out.println("gender : " + gender);
		System.out.println("hobby : " + sbHobby);
		System.out.println("favorite : " + favorite);
		System.out.println("desc : " + desc);
		
		// 브라우저에 보내기
		// use StringBuilder
		StringBuilder sb = new StringBuilder();
		sb.append("<h1>name : ").append(name).append("</h1>");
		sb.append("<h1>email : ").append(email).append("</h1>");
		sb.append("<h1>gender : ").append(gender).append("</h1>");
		sb.append("<h1>hobby : ").append(sbHobby).append("</h1>");
		sb.append("<h1>favorite : ").append(favorite).append("</h1>");
		sb.append("<h1>desc : ").append(desc).append("</h1>");
				
		response.getWriter().append(sb);
	}

}
