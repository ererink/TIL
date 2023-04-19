<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

  <title>IT's KB - register</title>
  <link rel="stylesheet" href="css/common.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  
  <style type="text/css">
     #register{
        padding: 20px 0;
     }
     #register h1{
      padding: 5px; 
      text-align: center;
     }
     
     #register form{
        /*background-color:pink;*/
       width: 100%;
       height: 300px;
       border: 1px solid lightgray;
       padding: 40px;
     }
     
     #register .form-item{
        margin-bottom: 10px;
     }
     
     #register .form-item label{
     display:inline-block;
       width: 150px;
       font-size: 18px;
     }
     
     #register .form-item input{
     display:inline-block;
       width: 250px;
       font-size: 18px;
     }
     
     #register button{
       float:right;
       padding: 5px;
       width: 100px;
       font-size: 18px;
       margin-top: 10px;
     }
  </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
    
  <script type="text/javascript">
  
     $(function(){
    	 $("#btnRegister").click(function(e){
    		 e.preventDefault();
    	    	
    	    	let name = $("#name").val();
    	    	let email =$("#email").val();
    	    	let phone = $("#phone").val();
    	    	let password = $("#password").val();
    	    	let password2 = $("#password2").val();
    	    	
    	    	console.log(name);
    	    	console.log(email);
    	    	console.log(phone);
    	    	console.log(password);
    	    	console.log(password2);
    	    	
    	    	if(password != password2){
    	    		alert("비밀번호 다르다.")
    	    		return;
    	    	}
    	    	
    	    	$.ajax({
            		url:"response.json",
            		type:"post",
            		dataType:"json",
            		success: function(data, status, xhr){
            			console.log(data);
            			if(data.result=="success"){
                			alert("가입 성공1");
                			 $("input").each(function(index, ele){
                    			//ele.value="";
                    			$(this).val("");
                    		})
                    		
            			}else
                			alert("가입 실패2")
            			
            		},
            		error : function(jqXHR, textStatus, errorThrown){
            			alert("문제 발생 : " + jqXHR.status)
            		}
            	
            		
            	});
    	    	
    	 });
     });
  
    
  </script>
  
</head>
<body>
<div id="container">


  <nav id="navbar">
    <!-- 5개의 메뉴생성 -->
      <ul>
        <li class="nav-item logo"><img src="images/logo.jpg" alt="로고입니다." ></li>
        <li class="nav-item"> <a href="personal.html">개인</a></li>
        <li class="nav-item"><a href="busines.html">기업</a></li>
        <li class="nav-item"><a href="login.html">로그인</a></li>
        <li class="nav-item"><a href="register.html">회원가입</a></li>
      </ul>
    </nav>
    
    <div id="banner">지금 당신의 행복! IT's KB Life!</div> 
    
  <div id="register">
	  <h1>Register</h1>
	  <form action="" method="post">
	  <div class="form-item">
	    <label for="name">이름</label>
	    <input type="text" id="name" name="name">
	 </div>
	    
	   <div class="form-item">
	    <label for="email">이메일</label>
	    <input type="email" id="email" name="email">
	  </div>
	  
	   <div class="form-item">
	    <label for="phone">연락처</label>
	    <input type="text" id="phone" name="phone">
	   </div>
	   
	    <div class="form-item">
		    <label for="password">비밀번호</label>
		    <input type="password" id="password" name="password">
	    </div>
	    
	   <div class="form-item">
		    <label for="password2">비밀번호 확인</label>
		    <input type="password" id="password2" name="password2">
	    </div>
	    
	    <hr>
	    <button id="btnRegister">회원 가입</button>
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