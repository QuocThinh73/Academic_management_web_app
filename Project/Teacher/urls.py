from django.urls import path
from . import views

app_name='Teacher'
urlpatterns = [
    path("", views.TeacherView.as_view(), name="teacher"),
    path("class_manage/", views.ClassManageView.as_view(), name='class_manage'),
    path("assessment/", views.AssessmentView.as_view(), name='Assessment'),
    path('upload/', views.UploadView.as_view(), name='upload'),
]