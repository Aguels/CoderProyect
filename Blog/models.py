from django.db import models
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class BlogEntry(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True, blank=True,null=True)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="blog",null=True,blank=True)

    def __str__(self):
        return f"{self.titulo}"