from django.urls import path
from . import views

app_name='File_document'
urlpatterns = [
    path("teacher/<int:course_id>/course_info/", views.AddDescription.as_view(), name = "AddDescription" ),
]