from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50,default="제목")
    created_at = models.DateTimeField(default=timezone.now)

    # 글 종류
    category = models.CharField(max_length=255)
    # 본문
    context = models.TextField(max_length=4000)
    # 작성자
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    # 글 이미지
    file = models.FileField(null=True)
    def __str__(self):
        return self.title