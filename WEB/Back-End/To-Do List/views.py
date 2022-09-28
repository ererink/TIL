from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # 모든 할일 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    todos = Todo.objects.all()

    # 2. template에 보내준다.
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


# DB에 저장
def create(request):
    # 1. parameter로 날라온 데이터를 받아서
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")

    # 2. DB에 저장한다.
    Todo.objects.create(content=content, priority=priority, deadline=deadline)

    context = {
        "content": content,
        "priority": priority,
        "deadline": deadline,
    }
    return redirect("todos:index")


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Todo.objects.get(id=pk).delete()

    return redirect("todos:index")
