from django.db import models

# Create your models here.


class ListeThemesEtudiant(models.Model): 
    Theme = models.CharField(max_length=126)
    Enseignant = models.CharField(max_length=126)
    Specialite = models.CharField(max_length=126)

