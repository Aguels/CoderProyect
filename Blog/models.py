from django.db import models
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image

class BlogEntry(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True, blank=True,null=True)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="blog",null=True,blank=True)

    def __str__(self):
        return f"{self.titulo}"

    def save(self):
        super().save()
        img = Image.open(self.imagen.path)
        if img.height > 1920 or img.width > 1080:
            new_img = (1920, 1080)
            img.thumbnail(new_img)
            img.save(self.imagen.path)