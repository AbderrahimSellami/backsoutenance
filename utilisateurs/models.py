from django.db import models

# Create your models here.

class Utilisateurs(models.Model):
    Utilisateur = models.CharField(max_length=256)
    Login = models.CharField(max_length=128)
    MDP = models.CharField(max_length=64)

class Soutenance (models.Model):
    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)
    specialite = models.CharField(max_length=256)
    theme = models.CharField(max_length=256)
    encadreur = models.CharField(max_length=256) 
    president = models.CharField(max_length=256)
    examinteur1 = models.CharField(max_length=256)
    examinteur2 = models.CharField(max_length=256)
    Date_debut = models.CharField(max_length=256)
    salle = models.CharField(max_length=256)