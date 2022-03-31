from django import forms
import django.contrib.auth.forms as djf

class mus(forms.Form):
    Nombre = forms.CharField(max_length=200)
    Rol = forms.CharField(max_length=200)

class registro(djf.UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)

class login(djf.AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
