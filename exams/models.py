# Create your models here.

from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Question(models.Model):

    question_text = models.CharField(max_length=500)

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_option = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text