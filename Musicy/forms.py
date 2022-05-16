from django import forms
import django.contrib.auth.forms as djf

class mus(forms.Form):
    Nombre = forms.CharField(max_length=200)
    Rol = forms.CharField(max_length=200)

class cargarPic(forms.Form):
    imagen = forms.ImageField()