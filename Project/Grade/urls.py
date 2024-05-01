from django.urls import path
from . import views

app_name='Grade'
urlpatterns = [
    path("<int:course_id>/import_score/", views.ImportScore.as_view(), name="ImportScore"),
]