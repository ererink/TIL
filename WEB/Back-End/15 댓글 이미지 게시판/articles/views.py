from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.

def index(request):
    articles = Article.objects.order_by('-pk')

    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
    else: 
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context=context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, '글이 수정되었습니다.')
            return redirect('articles:detail', article.pk)

    else:
        article_form = ArticleForm(instance=article)

    context = {
        'article_form': article_form
    }
    return render(request, 'articles/form.html', context)

def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()

    return redirect('articles:detail', article.pk)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")