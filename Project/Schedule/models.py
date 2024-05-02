from django.db import models
from Course.models import Course
# Create your models here.

class Schedule(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, null=True)
    