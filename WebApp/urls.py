from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url
from .views import home,contacto,nosotros,tratamientos,pacientes,login,registro


urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('tratamientos/', tratamientos, name='tratamientos'),
    path('pacientes/', pacientes, name='pacientes'),
    path('login/', login, name='login'),
    path('registro/', login, name='registro'),

]
