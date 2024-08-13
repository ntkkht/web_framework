from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    joined_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(choices= [("A", "Fantacy"), ("B", "Action"), (("C", "Survey"))], max_length=10, default="A")
    saleprice = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
