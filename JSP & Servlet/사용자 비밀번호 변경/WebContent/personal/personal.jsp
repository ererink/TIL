<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">

  <title>IT's KB - 개인</title>
  <link rel="stylesheet" href="css/common.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  
  <style>
	#change-pwd-form{
		border : 1px solid grey;
		width : 300px;
		height : 200px;
		margin: 200px auto;
	}
	*{
		box-sizing: border-box;
	
	}
	#change-pwd-form form{
	   width: 100%;
       height: 200px;
       border: 1px solid gray;
       padding: 40px;
	}
	#change-pwd-form .form-group label{
	   display:inline-block;
       width: 100px;
       font-size: 18px;
	}
	#change-pwd-form .form-group label{
	   display:inline-block;
       width: 200px;
       font-size: 18px;
	}
	#change-pwd-form button{
        float: right;
        width: 80px;
        font-size: 18px;
        padding: 5px;
     }
	.title{
		padding: 5px;
        text-align: center;
	}
	
</style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script type="text/javascript" src="${pageContext.request.contextPath}/js/common.js"></script>
  <script type="text/javascript">
	//비밀번호 변경 폼 보이기
	function showPasswordForm() {
	  var form = document.getElementById("change-pwd-form");
	  form.style.display = "block";
	}
	
	 // 비밀번호 변경 요청 보내기
	 function changePassword() {
	   var currentPwd = document.getElementById("current-password-input").value;
	   var newPwd = document.getElementById("new-password-input").value;
	   var newPwdConfirm = document.getElementById("new-password-confirm-input").value;
	
	    // 입력값 검증
	    if (currentPwd === "" || newPwd === "" || newPwdConfirm === "") {
	      alert("모든 항목을 입력해주세요.");
	      return;
	    }
	    if (newPwd !== newPwdConfirm) {
	      alert("새로운 비밀번호와 비밀번호 확인이 일치하지 않습니다.");
	      return;
	    }
	    
	    // Ajax
	    $(document).ready(function(){
	    	  $("#changePwdBtn").click(function(e){
	    	    e.preventDefault();
	    	    var currentPwd = $("#currentPwd").val();
	    	    var newPwd = $("#newPwd").val();
	    	    var confirmPwd = $("#confirmPwd").val();
	    	    var userSeq = $("#userSeq").val();
	    	    
	    	    $.ajax({
	    	      url: "user?action=changePwd",
	    	      type: "POST",
	    	      data: {
	    	        userSeq: userSeq,
	    	        currentPwd: currentPwd,
	    	        newPwd: newPwd,
	    	        confirmPwd: confirmPwd
	    	      },
	    	      success: function(response){
	    	        // 비밀번호 변경 성공
	    	        if(response == "1") {
	    	          alert("비밀번호가 변경되었습니다.");
	    	          location.reload();
	    	        } else {
	    	          // 비밀번호 변경 실패
	    	          alert("비밀번호 변경에 실패하였습니다.");
	    	        }
	    	      },
	    	      error: function(jqXHR, textStatus, errorThrown){
	    	        alert("비밀번호 변경 중 오류가 발생하였습니다. 잠시 후 다시 시도해주세요.");
	    	        console.log(textStatus, errorThrown);
	    	      }
	    	    });
	    	  });
	    	});
	</script>
  
</head>
<body>
<div id="container">

 	<jsp:include page="../navbar.jsp"/>
    <div id="banner">지금 당신의 행복! IT's KB Life!</div> 
    
    
  <h1 class="title">개인 페이지</h1>
  	<!-- 비밀번호 변경 버튼 -->
  	<a href="#" onclick="showPasswordForm()">비밀번호 변경하기</a>
  	
  	<!-- 비밀번호 변경 폼 -->
	<div id="change-pwd-form" style="display: none;">
	  <form>
	    <div class="form-group">
	      <label for="current-password-input">현재 비밀번호</label>
	      <input type="password" class="form-control" id="current-password-input">
	    </div>
	    <div class="form-group">
	      <label for="new-password-input">새로운 비밀번호</label>
	      <input type="password" class="form-control" id="new-password-input">
	    </div>
	    <div class="form-group">
	      <label for="new-password-confirm-input">새로운 비밀번호 확인</label>
	      <input type="password" class="form-control" id="new-password-confirm-input">
	    </div>
	    <button type="button" class="btn" onclick="changePassword()">변경하기</button>
	  </form>	  
	</div>
</div>
</body>
</html>