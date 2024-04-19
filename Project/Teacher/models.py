from django.db import models

# Create your models here.

class TeacherUser(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    department = models.CharField(max_length = 30, null = True, blank = True)