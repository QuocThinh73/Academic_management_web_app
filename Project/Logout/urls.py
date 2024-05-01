from django.urls import path
from . import views

app_name='Logout'
urlpatterns = [
    path("", views.Logout.as_view(), name="logout"),
]