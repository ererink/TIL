<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>IT's KB</title>
  <link rel="stylesheet" href="css/common.css">
  <link rel="stylesheet" href="css/navbar.css">
  <link rel="stylesheet" href="css/footer.css">
  <style type="text/css">
    #main{
      margin-top:5px;
      display: flex;
      justify-content: space-between; 
    }
    #main .main-item{
      width: 33%;
    }
    #main .main-item img{
     width: 100%;
    }
    
   /* #main .main-item h2{
    background-color:red;
      margin-top: 5px;
    }
    
    #main .main-item p{
      background-color:blue;
      margin-top: 5px;
    }*/
    
    #main .main-item button{
       float: right;
       padding: 5px;
       width: 80px;
       font-size: 15px;
    }
    
    
  </style>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script type="text/javascript" src="${pageContext.request.contextPath}/js/common.js"></script>
  
  <script type="text/javascript">
 
    $(function(){
    	//banner가져오기
    	getBanner("${pageContext.request.contextPath}");
    	
    	
    	 //버튼 클릭했을대
    	 $(".main-item-btn").click(function(){
    		 let idValue =  $(this).closest(".main-item").attr("data-main-item-id");
    		 console.log(idValue)
    	 });
    });//readyEnd
    
    
    
    
  
  </script>
</head>
<body>
  <div id="container">
    
   <!-- navbar -->
   <jsp:include page="navbar.jsp"/>
    
    <div id="banner">지금 당신의 행복! IT's KB Life!</div> 
    
    <div id="main" class="main-item">
    
     <!-- 총 3개의 서브영역 -->
      <div class="main-item" data-main-item-id="10">
        <img src="https://picsum.photos/200" alt="">
        <h2>제목1 : main-item 1</h2>
        <p>내용1</p>
        <button class="main-item-btn">button 1</button>
      </div>
      
      <div class="main-item" data-main-item-id="20">
        <img src="https://picsum.photos/200" alt="">
        <h2>제목2 : main-item 2</h2>
       <p>내용2</p>
        <button class="main-item-btn">button 2</button>
      </div>
      
      
      
      <div class="main-item" data-main-item-id="30">
        <img src="https://picsum.photos/200" alt="">
        <h2>제목3  : main-item 3</h2>
        <p>내용3.</p>
        <button class="main-item-btn">button 3</button>
      </div>
      
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