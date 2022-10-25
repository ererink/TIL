from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.CharField(max_length=80)
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True,
                                # processors=[ResizeToFill(400,300)],
                                # format='JPEG',
                                # options={'quality:80'},
                                null=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
