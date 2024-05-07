from django.db import models

# Create your models here.


class NonDispoEnseignant(models.Model): 
    Date = models.DateTimeField()
    Heure = models.TimeField() 

class ListeBinomes (models.Model): 
    Binome = models.CharField(max_length=126)
    Theme = models.CharField(max_length=126)
