from django.db import models

# Create your models here.

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Student(Person):
    roll_number = models.CharField(max_length=10)

class Teacher(Person):
    subject = models.CharField(max_length=50)