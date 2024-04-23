from django.db import models

# Create your models here.

class Planning(models.Model):
    Theme = models.CharField(max_length=256)
    Date = models.DateTimeField()
    Local = models.CharField(max_length=64)
    Binome = models.CharField(max_length=256)
    Encadreur = models.CharField(max_length=64)
    Jury = models.CharField(max_length=64)
