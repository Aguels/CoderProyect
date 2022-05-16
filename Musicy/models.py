from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Song(models.Model):
    nombre = models.CharField(max_length=200)
    letra = models.TextField()
    link = models.URLField()
    acordes = models.CharField(max_length=200)
    tono = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.nombre}"

class BlogEntry(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True, blank=True,null=True)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.titulo}"

class Musician(models.Model):
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre}, {self.rol}"

class Pic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="images",null=True,blank=True)