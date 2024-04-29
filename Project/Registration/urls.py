from django.urls import path
from .views import RegistrationStudent

app_name='Registration'
urlpatterns = [
    path("", RegistrationStudent.as_view(), name="registration_student"),
]