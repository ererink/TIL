# DB 필드와 HTML Form과 이어주는 가교 역할
# 사용자에게 받은 input을 유효성 검사를 거치게 해준다.

from django import forms

# models.py에 정의한 class(Article)을 불러온다.
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
