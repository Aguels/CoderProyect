from django.db import models

class Musician(models.Model):
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre}, {self.rol}"