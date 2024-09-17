from django.db import models

# Create your models here.
class Citizen(models.Model):
    citizenId = models.CharField(max_length=13)
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    expire_date = models.DateField()
    blood_type = models.CharField(max_length=2,choices= [("A", "A"), ("B", "B"), ("AB","AB"), ("O","O")])