from django.urls import path
from . import views

app_name='Assessment'
urlpatterns = [
    path("teacher/teacher_assess/<int:course_id>/", views.TeacherAssessmentView.as_view(), name="TeacherAssessment"),
    path("student/<int:student_id>/ViewAssessment", views.StudentAssessView.as_view(), name="StudentAssessView"),
]