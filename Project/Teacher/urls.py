from django.urls import path
from . import views

app_name='Teacher'
urlpatterns = [
    path("", views.TeacherView.as_view(), name="teacher"),
]