from django.db import models


class Maire(models.Model):
    nom = models.CharField(max_length=100, default='John')
    prenom = models.CharField(max_length=100, default='Doe')
    situation = models.CharField(max_length=1000, blank=True, default='Situation inconnue')
    date_de_naissance = models.DateTimeField()
    age = models.IntegerField(default=60)
    departement = models.CharField(max_length=100, default='departement inconnu')
    commune = models.CharField(max_length=100, default='Commune inconnu')
    civilite = models.CharField(max_length=3, default='Mme')

    class Meta:
        ordering = ('id', 'age')


class Region(models.Model):
    nom = models.CharField(max_length=100, default='John')
    code = models.CharField(max_length=100, default='75000')

    class Meta:
        ordering = ('id', 'code')
