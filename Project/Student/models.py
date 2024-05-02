from django.db import models
from Login.models import MyUser
from Databases.models import *

class Student(models.Model):
    student_id = models.CharField(max_length=15, null=False, primary_key=True, default='')
    name = models.CharField(max_length=30, null=True, default='')
    date_of_birth = models.DateField(null=True, default='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, null = True)
    username = models.OneToOneField(MyUser, on_delete=models.CASCADE,  null=True)

    def __str__(self):
        return self.name