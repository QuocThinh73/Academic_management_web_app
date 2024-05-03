from django.urls import path
from . import views

app_name='Student'
urlpatterns = [
    path("", views.StudentView.as_view(), name="student"),
    path("profile/", views.StudentProfile.as_view(), name="student_profile"),
    path("my_course/", views.StudentCourse.as_view(), name="student_course"),
    path("my_schedule/", views.ScheduleView.as_view(), name="student_schedule"),
]