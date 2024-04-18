from django.urls import path
from . import views

app_name='Login'
urlpatterns = [
    path("", views.StudentView.as_view(), name="student"),
]