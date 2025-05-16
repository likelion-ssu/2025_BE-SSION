from django.db import models

# Create your models here.

class student(models.Model):   
    name = models.CharField(max_length=150)
    studentid =  models.CharField(max_length=15)
    age = models.IntegerField()
    score = models.IntegerField()
    underage = models.BooleanField()
