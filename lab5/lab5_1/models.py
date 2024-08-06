from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    joined_date = models.DateField()

class Video(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
