from django.db import models

# Create your models here.
class Userdetails(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    place=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

