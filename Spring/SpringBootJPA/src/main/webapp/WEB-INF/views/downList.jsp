<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
  
 <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>   
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>다운로드 목록 </h2>
<h3>
<ul>
 <c:forEach items="${fileNames}" var="fileName">
     <li><a href="${pageContext.request.contextPath}/down.do?fileName=${fileName}">${fileName}</a></li> 
 </c:forEach>
 </ul>
</h3>



</body>
</html>















