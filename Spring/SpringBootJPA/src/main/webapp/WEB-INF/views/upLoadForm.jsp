<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>



<h2> 파일 업로드 기능 - Command객체 이용</h2>
<form action="upload" method="post" enctype="multipart/form-data">
	이름 : <input type="text" name="name"/><p>
	파일 첨부 : <input type="file" name="file"/>
	<input type="submit" value="전송"/>
</form>

<hr>

<h2> <a href="downList">파일List</a></h2>

</body>
</html>



