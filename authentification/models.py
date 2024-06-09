from django.db import models

# Create your models here.

class Admin(models.Model):
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=64)

class Teacher(models.Model):
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=64)

class Student(models.Model):
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password= models.CharField(max_length=64)
