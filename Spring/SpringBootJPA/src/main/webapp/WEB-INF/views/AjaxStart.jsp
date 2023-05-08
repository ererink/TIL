<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core"  prefix="c"%>
<!DOCTYPE html>
<html>
<head>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="js/jquery-3.6.1.min.js"></script>
<script type="text/javascript">
   $(function(){
	   alert("시작......")
	   
	   $("#loadBtn").click(function(){
		   $("#display").load("load");
	   });
	   ///////////////////////////////////
	   $("#ajaxBtn").click(function(){
		   $.ajax({
			   url: "ajax" , //서버요청주소
			   type: "post", //요청방식(get, post, put, delete, patch)
			   dataType: "text", //서버가 응답해주는 데이터타입 (text, html, xml, json)
			   data: "name=장희정", //서버에게 보낼 parameter정보 
			   success: function(result){
				   $("#display").html("<h3>"+result+"</h3>");
			   },
			   error : function(err){
				   alert(err+"에러 발생!!!")
			   }
				   
		   });
	   })
	   //////////////////////////////////////////////////
	   $("#jsonBtn").click(function(){
		   //alert(1)
		   $.ajax({
			   url: "json" , //서버요청주소
			   type: "post", //요청방식(get, post, put, delete, patch)
			   dataType: "json", //서버가 응답해주는 데이터타입 (text, html, xml, json)
			  // data: "name=장희정", //서버에게 보낼 parameter정보 
			   success: function(result){
				  // alert(result)
				  let str="";
				  $.each(result, function(index, item){
					  str+="<input type='checkbox' name='menu' value='"+ (index+1) +"'>" + item ;
				  })
				  $("#display").html(str);
			   },
			   error : function(err){
				   alert(err+"에러 발생!!!")
			   }
				   
		   });
	   })
	   ////////////////////////////////////////////////////
	   $("#dtoBtn").click(function(){
		   //alert(1)
		   $.ajax({
			   url: "memberDto" , //서버요청주소
			   type: "post", //요청방식(get, post, put, delete, patch)
			   dataType: "json", //서버가 응답해주는 데이터타입 (text, html, xml, json)
			  // data: "name=장희정", //서버에게 보낼 parameter정보 
			   success: function(result){
				  //alert(result)
				  
				  $("#display").html(result.id +" | " + result.name+" | " + result.age+" | " + result.addr);
				  
			   },
			   error : function(err){
				   alert(err+"에러 발생!!!")
			   }
				   
		   });
	   })
	   ////////////////////////////////////////////////////
	   $("#listBtn").click(function(){
		   $.ajax({
			   url: "memberList" , //서버요청주소
			   type: "post", //요청방식(get, post, put, delete, patch)
			   dataType: "json", //서버가 응답해주는 데이터타입 (text, html, xml, json)
			  // data: "name=장희정", //서버에게 보낼 parameter정보 
			   success: function(result){
				  //alert(result)
				  var str="<table>";
				  str+="<tr><td>번호</td><td>아이디</td><td>이름</td><td>나이</td><td>주소</td></tr>";
				  $.each(result, function(index, item){
					  str+="<tr>";
					  str+="<td>"+(index+1)+"</td>";
					  str+="<td>"+item.id+"</td>";
					  str+="<td>"+item.name+"</td>";
					  str+="<td>"+item.age+"</td>";
					  //str+="<td>"+item.addr+"</td>";
					  str+=`<td>${'${item.addr}'}</td>`;//템플릿문자열
					  str+="</tr>";
				  });
				  str+="</table>";
				  
				  $("#display").html(str);
			   },
			   error : function(err){
				   alert(err+"에러 발생!!!")
			   }
				   
		   });
	   })
	   /////////////////////////////////////////////////////////
	   
	   $("#mapBtn").click(function(){
		   $.ajax({
			   url: "map" , //서버요청주소
			   type: "post", //요청방식(get, post, put, delete, patch)
			   dataType: "json", //서버가 응답해주는 데이터타입 (text, html, xml, json)
			  // data: "name=장희정", //서버에게 보낼 parameter정보 
			   success: function(result){
				  alert(result.message)
				  alert(result.pageNo)
				  alert(result.dto +" , " + result.dto.id )
				  alert(result.memberList)
				  
				  $.each(result.memberList, function(index, item){
					   alert(item.id +" | " + item.age +" | " + item.addr);
				  });
				  
			   },
			   error : function(err){
				   alert(err+"에러 발생!!!")
			   }
				   
		   });
	   })
	   
	   
	   
   })//readyEnd
</script>
</head>
<body>

<input type="button" value="load함수" id="loadBtn">
<input type="button" value="ajax함수" id="ajaxBtn">
<input type="button" value="json결과" id="jsonBtn">

<input type="button" value="DTO결과" id="dtoBtn">
<input type="button" value="List<Member>결과" id="listBtn">
<input type="button" value="Map결과" id="mapBtn">


<hr>
<div id="display">  </div>



</body>
</html>



