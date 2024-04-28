from django.urls import path
from . import views

app_name='Teacher'
urlpatterns = [
    path("", views.TeacherView.as_view(), name="teacher"),
    path("teacher.html", views.TeacherView.as_view(), name="teacher"),
    path("class_manage.html", views.ClassManageView.as_view(), name='class_manage'),
    path('import_score/', views.ImportScoreView.as_view(), name='Import Score'),
    path("assessment.html", views.AssessmentView.as_view(), name='Assessment'),
    path('upload/', views.UploadView.as_view(), name='upload'),
]