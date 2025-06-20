from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField()
    publication_date = models.DateField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title