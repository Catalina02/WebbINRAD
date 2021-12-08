from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import registro,profile,logoutView
from django.conf.urls import include, url
from WebApp.views import home

app_name='AppUsers'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('registro/', registro, name='registro'),
  path('profile/', profile, name='profile'),
  url(r'^logout/$', logoutView, name='logout'),
]