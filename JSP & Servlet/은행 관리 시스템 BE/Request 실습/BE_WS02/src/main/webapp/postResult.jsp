<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>결과</title>
</head>
<body>
    <h2>전달된 데이터</h2>
    <table>
        <tr>
            <td>ID</td>
            <td><%= request.getParameter("id") %></td>
        </tr>
        <tr>
            <td>Name</td>
            <td><%= request.getParameter("name") %></td>
        </tr>
        <tr>
            <td>Email</td>
            <td><%= request.getParameter("email") %></td>
        </tr>
        <tr>
            <td>Gender</td>
            <td><%= request.getParameter("gender") %></td>
        </tr>
        <tr>
            <td>Hobby</td>
            <td><%= request.getParameter("hobby") %></td>
        </tr>
        <tr>
            <td>Favorite</td>
            <td><%= request.getParameter("favorite") %></td>
        </tr>
        <tr>
            <td>Desc</td>
            <td><%= request.getParameter("desc") %></td>
        </tr>
    </table>
</body>
</html>
