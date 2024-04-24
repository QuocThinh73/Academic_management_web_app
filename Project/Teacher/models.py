from django.db import models
from Login.models import MyUser
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    department = models.CharField(max_length = 30, null = True, blank = True)
    username = models.OneToOneField(MyUser, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name