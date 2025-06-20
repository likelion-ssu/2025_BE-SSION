from django.db import models
from bookapp.models import Book

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) #처음 생설될 떄의 날짜와 시간 저장
    updated_at = models.DateTimeField(auto_now=True) #객체 저장할 때마다 날짜와 시간 갱신
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.title