from django.db import models

# Create your models here.

class utilisateurs(models.Model):
    Utilisateur = models.CharField(max_length=256)
    Login = models.CharField(max_length=128)
    MDP = models.CharField(max_length=64)