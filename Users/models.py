from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatar",null=True,blank=True)
    def __str__(self):
        return f"{self.user}"   
    def save(self):
        super().save()
        img = Image.open(self.imagen.path)
        if img.height > 150 or img.width > 150:
            new_img = (150, 150)
            img.thumbnail(new_img)
            img.save(self.imagen.path)