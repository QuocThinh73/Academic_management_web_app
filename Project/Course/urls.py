from django.urls import path
from . import views

app_name='Course'
urlpatterns = [
    path("student/<int:course_id>/", views.CourseStudent.as_view(), name="CourseStudent"),
    path("student/<int:course_id>/score_view/", views.ScoreView.as_view(), name="ScoreView"),
<<<<<<< HEAD
=======
    path("student/<int:course_id>/document_view/", views.DocumentView.as_view(), name="DocumentView"),
>>>>>>> 633c4d74cd88f5066f0024bcccfab65bf130dc1e
    path("teacher/<int:course_id>/", views.CourseTeacher.as_view(), name="CourseTeacher"),
    path("teacher/<int:course_id>/list_of_student/", views.ListOfStudent.as_view(), name="ListOfStudent"),
    path("teacher/<int:course_id>/assessment/", views.Assessment.as_view(), name="Assessment"),
]