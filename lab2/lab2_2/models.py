from django.db import models

# Create your models here.
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255, blank=False)
    published_date = models.DateField()
    short_detail = models.CharField(max_length=300, blank=False)
    demo = models.BooleanField()

class Author(models.Model):
    id = models.CharField(max_length=13, auto_created=False, primary_key=True)
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    phone = models.CharField(max_length=10, blank=True)
    joined_date = models.DateField()