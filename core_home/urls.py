from django.urls import path
from . import views

#URL Configuration
urlpatterns = [
    path('', views.home),
    path('core_home/templates/login.html', views.login),
]