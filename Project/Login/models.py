from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    USER_TYPE_CHOICES = [
         ('Student', 'Student'),
         ('Teacher', 'Teacher'),
         ('Admin', 'Admin'),
     ]
    user_type = models.CharField(max_length = 20, choices = USER_TYPE_CHOICES, default = "Student")
