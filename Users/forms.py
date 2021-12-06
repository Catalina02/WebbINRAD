from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=['rut','dv','nombre','apellido_paterno','apellido_materno','email','telefono_contacto','password1','password2']
        