from django.urls import path
from django.contrib.auth.decorators import login_required

from Users.views import RegistrarUsuario
urlpatterns = [
    path('registrar_usuario/', login_required(RegistrarUsuario.as_view(),name='registrar_usuario'))
]