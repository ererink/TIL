<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>post</title>
    <style>
      button{
        height: 26px
      }
    </style>
  </head>
  <body>

    <form action="">
      <h4>기본 정보</h4>
      <label for="name">이름</label><br>
      <input id="name" name="name" type="text"/><br>
      <label for="email">e-mail</label><br>
      <input id="email" name="email" type="email"/><br>

      <h4>성별</h4>
      <input id="male" type="radio" name="gender" value="M"><label for="male">남</label>
      <input id="female" type="radio" name="gender" value="F" checked><label for="female">여</label><br>

      <h4>취미</h4>
      <input id="movie" type="checkbox" name="hobby" value="movie">
      <label for="movie">영화</label>        
      <input id="sport" type="checkbox" name="hobby" value="sport" checked>
      <label for="sport">스포츠</label>
      <input id="music" type="checkbox" name="hobby" value="music">
      <label for="music">음악</label>

      <h4>선호하는 재테크</h4>
      <select name="favorite" id="favorite">
          <option value="SV">저축</option>
          <option value="ST" selected>주식</option>
          <option value="PS">연금</option>
      </select>
      
      <h4>기타</h4>
      <textarea name="desc" id="desc" cols="30" rows="5"></textarea>
    </form>

    <hr>
    <button id="btnSendPost">Post 전송</button>

    <script>

        window.onload = function(){
        	
          // Post 전송 코드를 작성하세요.
          document.querySelector("#btnSendPost").onclick = function(){
            let form = document.querySelector("form");
            form.action = "params";
            form.method = "post";
            form.submit();
          };

        };
    </script>
  </body>
</html>
