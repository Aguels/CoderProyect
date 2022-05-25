from django import forms
import django.contrib.auth.forms as djf
from django.core.exceptions import ValidationError

class Registro(djf.UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    class Meta:
        model = djf.User
        fields = ["username","email","password1","password2","first_name","last_name"]

class Login(djf.AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput)

class EditUser(djf.UserChangeForm):
    email = forms.EmailField(label="Correo")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password = None
    class Meta:
        model = djf.User
        fields = ["email","first_name","last_name"]

class EditPass(djf.SetPasswordForm):
    new_password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Repita la contraseña",widget=forms.PasswordInput)
    class Meta:
        model = djf.User
        fields = ["new_password1","new_password2"]

class CargarAvatar(forms.Form):
    imagen = forms.ImageField()