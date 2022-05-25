from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from PIL import Image

def validate_image(imagen):
    max_height = 150
    max_width = 150
    height = imagen.file.height
    width = imagen.file.width
    if width > max_width or height > max_height:
        raise ValidationError("El tamaño de la imagen excede los 150 pixeles en alguno de sus ejes")
    return validate_image

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatar",null=True,blank=True, validators=[validate_image])
    def __str__(self):
        return f"{self.user}"   
    def save(self):
        super().save()
        img = Image.open(self.imagen.path)
        if img.height > 150 or img.width > 150:
            new_img = (150, 150)
            img.thumbnail(new_img)
            img.save(self.imagen.path)