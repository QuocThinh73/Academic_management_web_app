from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name
    
class Student(AbstractUser):
    sex_choice = ((0, "Nữ"), (1, "Nam"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice, default=0)
    faculty = models.CharField(default='', max_length=100)
    GPA = models.FloatField(default=0)


