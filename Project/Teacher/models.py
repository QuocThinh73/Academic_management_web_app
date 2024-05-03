from django.db import models
from Login.models import MyUser
from Databases.models import Department

class Degrees(models.Model):
    university = models.CharField(max_length=100)
    year_obtained = models.IntegerField(null=True, default=2010)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, null=True, blank=True)
    major = models.CharField(max_length=40, null=True)

    TYPE_CHOICES = [
         ('Cử nhân', 'Cử nhân'),
         ('Thạc sĩ', 'Thạc sĩ'),
         ('Tiến sĩ', 'Tiến sĩ'),
     ]
    type = models.CharField(max_length=20, null=True, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    username = models.OneToOneField(MyUser, on_delete=models.CASCADE, null = True)

    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ]
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
    
    