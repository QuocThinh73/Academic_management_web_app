from django.urls import path
from . import views
app_name='Course'
urlpatterns = [
    path("student/<int:course_id>/", views.CourseStudent.as_view(), name="CourseStudent"),
    path("student/<int:course_id>/score_view/", views.ScoreView.as_view(), name="ScoreView"),
    path("student/<int:course_id>/document_view/", views.DocumentView.as_view(), name="DocumentView"),
    path("teacher/<int:course_id>/", views.CourseTeacher.as_view(), name="CourseTeacher"),
    path("teacher/<int:course_id>/list_of_student/", views.ListOfStudent.as_view(), name="ListOfStudent"),
    path("teacher/<int:course_id>/assessment/", views.Assessment.as_view(), name="Assessment"),
    path("course/<int:course_id>/documents/", views.DocumentView.as_view(), name="DocumentView"),
]