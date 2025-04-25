from django.db import models

# Create your models here.

class Personagens(models.Model):
    id_personagem = models.IntegerField(blank=True)
    nome = models.CharField(max_length=200)
    status = models.BooleanField(null=True, blank=True)
    especie = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    



    def __str__(self):
        return self.title
