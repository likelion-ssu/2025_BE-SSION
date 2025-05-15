from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=150)
    student_number = models.CharField(max_length=20)
    grade = models.IntegerField()
