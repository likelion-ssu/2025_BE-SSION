from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    studentId = models.CharField(max_length=10)
    phoneNum = models.CharField(max_length=15)
    age = models.IntegerField()
    email = models.CharField(max_length=30)