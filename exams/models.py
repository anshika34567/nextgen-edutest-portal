# Create your models here.

from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#QUESTION MODEL
class Exam(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    total_questions = models.IntegerField()
    time_limit = models.IntegerField(help_text="Time in minutes")
    
    def __str__(self):
        return self.title


    
class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text



#RESULT MODEL
class Result(models.Model):

    student_name = models.CharField(max_length=100)
    score = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name
    
    