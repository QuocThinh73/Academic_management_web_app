from django.urls import path
from . import views

app_name='Assessment'
urlpatterns = [
    path("teacher/teacher_assess/<int:course_id>/", views.TeacherAssessmentView.as_view(), name="TeacherAssessmentView"),
    path("student/<int:pk>/ViewAssessment/", views.StudentAssessView.as_view(), name="StudentAssessView"),
    path("student/student_assess/<int:course_id>/", views.StudentAssessmentView.as_view(), name="StudentAssessmentView"),
    path("teacher/<int:course_id>/ViewAssessment/", views.TeacherAssessView.as_view(), name="TeacherAssessView"),
]