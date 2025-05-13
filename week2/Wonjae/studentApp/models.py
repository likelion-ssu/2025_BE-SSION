from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    studentId = models.IntegerField()
    grade = models.IntegerField()
    age = models.IntegerField()
    major = models.CharField(max_length=150)
    email = models.EmailField()