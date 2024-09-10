from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
