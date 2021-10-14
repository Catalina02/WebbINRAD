from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url


urlpatterns = [
    path('', views.inicio, name='inicio'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
