from django.db import models

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    anio = models.IntegerField()
    
    def __str__(self):
        return self.titulo
