from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .views import registro
app_name='AppUsers'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(), name='login'),
  path('registro/', registro, name='registro'),
]