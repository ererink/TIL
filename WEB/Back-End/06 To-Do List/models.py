from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=80)
    priority = models.IntegerField(default=3)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
