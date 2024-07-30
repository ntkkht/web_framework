from django.db import models

# Create your models here.

class BusinessContact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.address}'

class Author(models.Model):
    id = models.CharField(primary_key = True, max_length=13, auto_created=False)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    joined_date = models.DateField()
    contact = models.OneToOneField(BusinessContact, on_delete=models.CASCADE, default="")

class Video(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    
class Course(models.Model):
    title = models.CharField(max_length=150)
    video = models.ManyToManyField(Video, default="",related_name= "videos", related_query_name= "q_video")

    def __str__(self):
        return self.title

