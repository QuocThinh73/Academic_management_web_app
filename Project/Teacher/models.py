from django.db import models
from Login.models import MyUser
from Databases.models import Department

class Degrees(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year_obtained = models.IntegerField(default=4)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    username = models.OneToOneField(MyUser, on_delete=models.CASCADE, null = True)
    teaching_schedule = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    