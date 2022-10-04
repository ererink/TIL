# 앱의 모든 필드를 가져다 쓰겠다.
# model form의 인스턴스로 넘겨준다.

from django import forms
from .models import Recap


class RecapForm(forms.ModelForm):
    class Meta:
        model = Recap
        # title, content만 넘겨준다.
        fields = ["title", "content"]
