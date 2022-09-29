from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY
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


def detail(request, pk):
    # 특정 pk의 데이터를 가져온다.
    todo = Todo.objects.get(id=pk)
    context = {
        "todo": todo,
    }
    return render(request, "todos/detail.html", context)


def edit(request, pk):
    post = Todo.objects.get(id=pk)
    complted = request.GET.get("complted")
    context = {
        "post": post,
        "complted": complted,
    }
    return render(request, "todos/edit.html", context)


# def edit(request, pk):
#     change = todos.objects.get(id=pk)
#     completed = request.GET.get('completed')
#     if completed == True:
#         change.completed = False
#     else:
#         change.completed = True

#     change.save()
#     return redirect('todos:index')


def update(request, pk):
    # update할 특정 데이터를 가져온다.
    post = Todo.objects.get(id=pk)

    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    completed = request.GET.get("completed")

    # 수정하기
    post.content = content
    post.priority = priority
    post.deadline = deadline
    post.completed = completed

    post.save()
    return redirect("todos:detail", post.pk)
