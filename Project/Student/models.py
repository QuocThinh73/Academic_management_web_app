from django.db import models

# Create your models here.

class StudentUser(models.Model):
    student_id = models.CharField(max_length=30, null=True, default='')
    date_of_birth = models.DateField(null = True, blank = True)
    major = models.CharField(max_length = 50, null = True, blank = True)
    enrollment_date = models.DateField(null = True, blank = True)