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
    hometown = models.CharField(max_length=40, null=True)

    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ]
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)

    STATE_CHOICES = [
        ('Đang học', 'Đang học'),
        ('Tạm dừng học', 'Tạm dừng học'),
        ('Thôi học', 'Thôi học'),
        ('Tốt nghiệp', 'Tốt nghiệp'),
    ]
    state = models.CharField(max_length=20, null=True, choices=STATE_CHOICES)

    TYPE_CHOICES = [
        ('Cử nhân', 'Cử nhân'),
        ('Thạc sĩ', 'Thạc sĩ'),
    ]
    type = models.CharField(max_length=20, null=True, choices=TYPE_CHOICES)


    def __str__(self):
        return self.name