from django.db import models
from bookapp.models import Book

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.title