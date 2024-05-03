from django.db import models
from Course.models import Course
# Create your models here.
class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    description = models.TextField(null = True)
    syllabus = models.TextField(null = True)
    course_file = models.FileField(upload_to='Course/course_file/', null = True, blank=None)
