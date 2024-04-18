from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    pass

class StudentUser(MyUser):
    student_id = models.CharField(max_length=30)
    user_type = "Student"

class TeacherUser(MyUser):
    teacher_id = models.CharField(max_length=30)
    user_type = "Teacher"
