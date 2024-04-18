from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class StudentUser(MyUser):
    student_id = models.CharField(max_length=30)
    is_student = True

class TeacherUser(MyUser):
    teacher_id = models.CharField(max_length=30)
    is_teacher = True
