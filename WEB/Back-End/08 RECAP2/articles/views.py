from django.shortcuts import render, redirect

# DB 가져오기
from .models import Article

# forms.py 불러오기
from .forms import ArticleForm

# Create your views here.
def index(request):
    # DB에 저장된 데이터를 articles로 불러온다.
    articles = Article.objects.order_by("created_at")

    # templates(index.html)에 전달한다.
    context = {
        "articles": articles,
    }
    return render(request, "articles/index.html", context)


def new(request):
    return render(request, "articles/new")


# 생성
def create(request):
    # DB에 데이터 보내기 (저장)
    # 유효성 검사(is_valid())
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")

    else:
        article_form = ArticleForm()

    context = {
        "article_form": article_form,
    }
    return render(request, "articles/new.html", context=context)


def detail(request, pk):
    # 특정 글 가져오기
    article = Article.objects.get(pk=pk)

    context = {
        "article": article,
    }
    return render(request, "articles/detail.html", context)


# 수정
def update(request, pk):
    # 특정 글 가져오기
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # 받은 데이터를 인스턴스로 넘겨주기
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", article.pk)

    else:
        article_form = ArticleForm(instance=article)

    context = {
        "article_form": article_form,
    }
    return render(request, "articles/update.html", context)


# 삭제
def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")
