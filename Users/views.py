from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from Users.models import Usuario
from .forms import FormularioUsuario
from django.urls import reverse_lazy
# Create your views here.


class RegistrarUsuario(CreateView):
    model=Usuario
    form_class=FormularioUsuario
    template_name = 'User/crear_usuario.html'
    success=reverse_lazy('usuarios:listar_usuarios')