from django.db import models

# Create your models here.

class Admin(models.Model):
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=64)