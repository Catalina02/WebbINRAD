from Apps.users.views import RegistroUsuario
from django.conf.urls import url

urlpatterns=[
    url(r'^registrar',RegistroUsuario.as_view(),name='registar')


]