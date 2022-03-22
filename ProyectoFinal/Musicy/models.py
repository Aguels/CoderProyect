from asyncio.windows_events import NULL
from django.db import models

class Song(models.Model):
    nombre = models.CharField(max_length=200)
    letra = models.TextField()
    link = models.URLField()
    acordes = models.TextField()

class BlogEntry(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()

class Musician(models.Model):
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
