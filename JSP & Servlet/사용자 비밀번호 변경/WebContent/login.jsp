<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

  <title>IT's KB - login</title>
  <link rel="stylesheet" href="css/common.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  
  <style type="text/css">
     #login{
       padding: 20px 0;
     }
     #login h1{
       padding: 5px;
       text-align: center;
     }
     
     #login form{
    
       width: 100%;
       height: 200px;
       border: 1px solid gray;
       padding: 40px;
     }
     
     #login .form-item{
        margin-bottom: 10px;
     }
     
     #login .form-item label{
     display:inline-block;
       width: 100px;
       font-size: 18px;
     }
     
     #login .form-item input{
     display:inline-block;
       width: 200px;
       font-size: 18px;
     }
     
     #login button{
        float: right;
        width: 80px;
         font-size: 18px;
         padding: 5px;
     }
     
  </style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script type="text/javascript" src="${pageContext.request.contextPath}/js/common.js"></script>
  
  <script type="text/javascript">
  
     $(function(){
    	 
    	 //banner가져오기 
    	 getBanner("${pageContext.request.contextPath}");
    	 
    	 
    	 $("#btnLogin").click(function(e){
    		 e.preventDefault();
    		 
    		 let email =   $("#email") ;
     		 let pwd =   $("#password");
     		 
        
    		 if(email.val()==""){
  			   alert("이메일를 입력해주세요.");
  			   email.focus();
  			   return false;
  		    }
  		
	  		if(pwd.val()==""){
	  			alert("비밀번호를 입력해주세요.");
	  			pwd.focus();
	  			return false;
	  		}
	  		
    		
    		$.ajax({
        		url:"${pageContext.request.contextPath}/login",
        		type:"post",
        		dataType:"json", //응답결과 json
        		//data:"email=값&pass=값" , //queryStirng
        		data:{email:email.val(), pass:pwd.val()},
        		success: function(data){
        			console.log(data);
        			if(data.result=="success"){
            			location.href="${pageContext.request.contextPath}/index.jsp";
        			}else{
            			alert("정보를 다시확인해주세요.");
            			$("input").val("");
            			$("#email").focus();
        			}
        			
        		},
        		error : function(jqXHR, textStatus, errorThrown){
        			alert("문제 발생 : " + jqXHR.status)
        		}
        	
        		
        	});//ajaxEnd
     		
    	 });//클릭끝
     });
  
   
  
  </script>
</head>
<body>
<div id="container">

 <jsp:include page="navbar.jsp"/>
    
    <div id="banner">지금 당신의 행복! IT's KB Life!</div> 
 
 <div id="login">
  <h1>Login</h1>
  <form action="" method="post">
   <div class="form-item">
    <label for="email">이메일</label>
    <input type="text" id="email" name="email">
    </div>
   
   <div class="form-item">
    <label for="password">비밀번호</label>
    <input type="password" id="password" name="password">
    </div>
    
    <hr>
    <button id="btnLogin">로그인</button>
  </form>
</div>   

  
    <footer>
      <ul>
        <li>서울시 선릉역 We-Work</li>
        <li>02-0000-0000</li>
      </ul>
    </footer>
    
 </div>
</body>
</html>