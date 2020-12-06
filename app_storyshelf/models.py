from django.db import models

# Create your models here.

class W_Saying(models.Model):
    saying = models.CharField(max_length=50)
    author = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

class Content(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)