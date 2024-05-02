from django.urls import path
from . import views

app_name='Course'
urlpatterns = [
    path("student/<int:course_id>/", views.CourseStudent.as_view(), name="CourseStudent"),
    path("teacher/<int:course_id>/", views.CourseTeacher.as_view(), name="CourseTeacher"),
    path("teacher/<int:course_id>/list_of_student/", views.ListOfStudent.as_view(), name="ListOfStudent"),
    path("teacher/<int:course_id>/course_info/", views.AddDescription.as_view(), name = "AddDescription" ),
]