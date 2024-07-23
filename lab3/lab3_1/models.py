from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, blank = True)
    joined_date = models.DateField()
    type_author = models.CharField(choices= [("A", "Fulltime"), ("B", "Parttime")], max_length=10, default="A")
    
    def getType(self):
        return self.type_author
    def getPhone(self):
        return self.phone
    def getData(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'phone': self.phone,
            'joined_date': self.joined_date,
            'type': self.type_author
        }

class Video(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    short_detail = models.CharField(max_length = 300)
    demo = models.BooleanField(default=False)

    def getTitle(self):
        return self.title
    def getDemo(self):
        return self.demo
    def getData(self):
        return {
            'title': self.title,
            'published_date': self.published_date,
            'short_detail': self.short_detail,
            'demo': self.demo
        }