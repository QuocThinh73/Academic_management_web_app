from django.urls import path
from . import views

app_name='Teacher'
urlpatterns = [
    path("", views.TeacherView.as_view(), name="teacher"),
    path("class_manage/", views.ClassManageView.as_view(), name='class_manage'),
    path('profile/', views.TeacherProfile.as_view(), name='TeacherProfile'),
    path('schedule/', views.TeacherSchedule.as_view(), name='TeacherSchedule'),
]