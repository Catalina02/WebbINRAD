from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
app_name='AppUsers'

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(), name='login'),
]