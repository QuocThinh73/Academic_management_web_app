
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('Login/', views.LoginClass.as_view(), name='login'),
    path('viewuser/', views.ViewUser.as_view(), name='viewuser')
]
