from django.db import models

# Create your models here.

class Planning(models.Model):
    Theme = models.CharField(max_length=256)
    Date = models.DateTimeField()
    Local = models.CharField(max_length=64)
    Binome = models.CharField(max_length=256)
    Encadreur = models.CharField(max_length=64)
    Jury = models.CharField(max_length=64)


class Plateforme(models.Model):
    Date_debut=models.DateTimeField()
    Date_fin=models.DateTimeField()
    heure_debut=models.TimeField() 
    heure_fin=models.TimeField() 
    duree=models.TimeField() 
    salle=models.CharField(max_length=64)


