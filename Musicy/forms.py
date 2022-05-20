from django import forms

class CargarPic(forms.Form):
    imagen = forms.ImageField()