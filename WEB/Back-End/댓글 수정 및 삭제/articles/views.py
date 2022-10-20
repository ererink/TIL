from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
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
            article = article_form.save(commit=False)
            article.user = request.user 
            article.save()
            messages.success(request, '게시물 작성 완료!')
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
    updated_comment = CommentForm(request.POST, instance=article)

    context = {
        'article': article,
        'comments': article.comment_set.all(),
        'comment_form': comment_form,
        'updated_comment': updated_comment,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user: 
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
    else:

        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)

@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()

    return redirect('articles:detail', article.pk)

def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")

def comments_delete(request, article_pk, comment_pk):
     Comment.objects.get(pk=comment_pk).delete()
     return redirect('articles:detail', article_pk)

def comments_update(request, article_pk, comment_pk):
    article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == "POST":
        updated_comment = CommentForm(request.POST, instance=comment)
        if updated_comment.is_valid():
            comment.content = updated_comment
            comment.article = article
            comment.save()
            messages.success(request, "댓글 수정 완료")
            return redirect("articles:detail", article.pk)
            
        else:
            comment_form = CommentForm(instance=comment)

        context = {
            'comment_form': comment_form
        }
        return render(request, "articles/comment_update.html", context) 

    else:
        return redirect('articles:detail', article.pk, comment.pk)
    
    # updated_comment = request.POST.get("updated_comment")

    # if request.user != comment.user:
    #     messages.warning(request, "권한이 없습니다.")
    #     return redirect("articles:detail", article_pk)

    # if request.user == comment.user:
