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
<h3>업로드 결과 </h3>
<h4>
 작성자 :${name} <br>
 첨부파일이름 :${originalFilename}  <br>
 경로 : ${path}<br>
 파일사이즈 :${fileSize} <br>
</h4>

<hr>
<h3>업로드 결과 - UploadDTO </h3>
<h4>
 작성자 :${uploadDTO.name} <br>
 첨부파일이름 :${uploadDTO.file.originalFilename}  <br>
 파일사이즈 :${uploadDTO.file.size} <br>
 
 UploadDTO의 fileName속성: ${uploadDTO.fileName}<br> 
 UploadDTO의 fileSize속성 : ${uploadDTO.fileSize}<br> 
</h4>
<img src="${pageContext.request.contextPath}/images/${uploadDTO.file.originalFilename}">

</body>
</html>













