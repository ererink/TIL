<%@ page import="dto.UserDto" %>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
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
  <script type="text/javascript">
  
     $(function(){
    	 
    	 $("#btnLogin").click(function(e){
    		 e.preventDefault();
    		 
    		 let id =   $("#id").val() ;
     		 let pwd =   $("#password").val();
     		 
     		console.log(id)
    		console.log(pwd)
    		
    		$.ajax({
        		url:"response.json",
        		type:"post",
        		dataType:"json",
        		data: { email: id, password: pwd },
        		success: function(data, status, xhr){
        			console.log(data);
        			if(data.result=="success")
        				location.href = "index.jsp";
            		else
            			alert("�α��� ����2")
        			
        		},
        		error : function(jqXHR, textStatus, errorThrown){
        			alert("���� �߻� : " + jqXHR.status)
        		}
        	
        		
        	});
     		
    	 });//Ŭ����
     });
  
   
  
  </script>
</head>
<body>

<div id="container">
  <%@ include file="navBar.jsp" %>
    
    <div id="banner">���� ����� �ູ! IT's KB Life!</div> 
 
 <div id="login">
  <h1>Login</h1>
  <form action="" method="post">
   <div class="form-item">
    <label for="id">���̵�</label>
    <input type="text" id="id" name="id">
    </div>
   
   <div class="form-item">
    <label for="password">��й�ȣ</label>
    <input type="password" id="password" name="password">
    </div>
    
    <hr>
    <button id="btnLogin">�α���</button>
  </form>
</div>   

  
    <footer>
      <ul>
        <li>����� ������ We-Work</li>
        <li>02-0000-0000</li>
      </ul>
    </footer>
    
 </div>
</body>
</html>