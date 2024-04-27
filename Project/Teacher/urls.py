from django.urls import path
from . import views

app_name='Teacher'
urlpatterns = [
    path("", views.TeacherView.as_view(), name="teacher"),
    path("class_manage/", views.ClassManageView.as_view(), name='Class Manage'),
    path('import_score/', views.ImportScoreView.as_view(), name='Import Score'),
    path('assessment/', views.AssessmentView.as_view(), name='assessment'),
    path('upload/', views.UploadView.as_view(), name='upload'),
]