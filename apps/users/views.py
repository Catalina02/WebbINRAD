from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class RegistroUsuario(CreateView):
    model=User
    template_name='user/templates/register.html'
    form_class=UserCreationForm
    #success_url=reverse_lay('app:app_lista')