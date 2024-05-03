from django.urls import path
from . import views

app_name='Assessment'
urlpatterns = [
    path("teacher/<int:course_id>/teacher_assess/<int:student_id>/", views.TeacherAssessmentView.as_view(), name="TeacherAssessment"),
    path("student/<int:student_id>/ViewAssessment", views.StudentAssessView.as_view(), name="StudentAssessView"),
]