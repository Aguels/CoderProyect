from django import forms

class cargarPic(forms.Form):
    imagen = forms.ImageField()