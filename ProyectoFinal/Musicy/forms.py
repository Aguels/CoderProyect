from socket import fromshare
from django import forms

class inputmus(forms.Form):
    Nombre = forms.CharField(max_length=200)
    Rol = forms.CharField(max_length=200)

