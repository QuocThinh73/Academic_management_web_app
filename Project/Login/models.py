from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class StudentUser(AbstractUser):
    user_type = "Student"

class TeacherUser(AbstractUser):
    user_type = "Teacher"
