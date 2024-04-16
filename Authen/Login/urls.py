
from django.urls import path
from . import views

app_name='Login'
urlpatterns = [
    path('', views.IndexClass.as_view(), name='index'),
    path('Login/', views.LoginClass.as_view(), name='login'),
    path('viewuser/', views.ViewUser.as_view(), name='viewuser'),
    path('viewscore/', views.view_score, name='viewscore'),
    path('add_post/', views.AddPost.as_view(), name='add_post')
]
