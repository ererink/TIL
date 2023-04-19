<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link rel="stylesheet" href="css/navbar.css">

</head>
<body>

  <nav id="navbar">
    <!-- 5개의 메뉴생성 -->
      <ul>
        <li class="nav-item logo"><img src="images/logo.jpg" alt="로고입니다." ></li>
        <li class="nav-item"> <a href="personal.html">개인</a></li>
        <li class="nav-item"><a href="busines.html">기업</a></li>
        <%
		    String userId = (String)session.getAttribute("userId");
		    if (userId == null) {
		%>
       		<li><a href="login.jsp">로그인</a></li>
		<%
		    } else {
		%>
	        <li><a href="#" onclick="logout()">로그아웃</a></li>
		<%
		    }
		%>
        <li class="nav-item"><a href="register.html">회원가입</a></li>
      </ul>
    </nav>

</body>
</html>