from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    studentId = models.IntegerField()
    age = models.IntegerField()
    grade = models.IntegerField()
    major = models.CharField(max_length=50)
    email = models.EmailField()
