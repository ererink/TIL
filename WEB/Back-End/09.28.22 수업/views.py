from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    # 모든 글 목록을 보여준다.
    # 1. DB에서 모든 글을 불러온다.
    posts = Post.objects.all()
    # 2. template에 보내준다.
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def new(request):
    return render(request, "posts/new.html")


def create(request):
    # DB에 저장하는 로직을 쓴다.
    # 1. parameter로 날라온 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 2. DB에 저장한다.
    Post.objects.create(title=title, content=content)

    context = {"title": title, "content": content}

    return redirect("posts:index")
    # 새 글을 쓰면 바로 메인페이지인 index로 간다.


def delete(request, pk):
    # pk에 해당하는 글 삭제
    Post.objects.get(id=pk).delete()
    return redirect("posts:index")
