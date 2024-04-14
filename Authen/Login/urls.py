
from django.urls import path
from . import IndexClass, LoginClass

urlpatterns = [
    path("", IndexClass.as_view(), name='index'),
    path("Login/", LoginClass.as_view(), name='login'),
]
