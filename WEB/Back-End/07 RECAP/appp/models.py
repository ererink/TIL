from django.db import models

"""
제목: 20글자 이내
내용: 제한 없음
작성시간: 자동(현재시간)
수정시간: 자동
"""

# Create your models here.
class Recap(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
