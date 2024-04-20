from django.db import models
from Login.models import MyUser

# Create your models here.

class Student(models.Model):
    id = models.CharField(max_length=15, null=False, primary_key=True, default='')
    name = models.CharField(max_length=30, null=True, default='')
    date_of_birth = models.DateField(null = True, default='')
    department = models.CharField(max_length = 50, null = True, default='')
    major = models.CharField(max_length = 50, null = True, default='')
    enrollment_date = models.DateField(null = True, default='')
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name