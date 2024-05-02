from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50, null=True, default="")
    credit = models.IntegerField(default=0)
    days = models.IntegerField(default=1)
    hours = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50, null=True, default="")

    def __str__(self):
        return self.name
    
class Major(models.Model):
    name = models.CharField(max_length=50, null=True, default="")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Semester(models.Model):
    semester_id = models.CharField(max_length=10, null=True, default="")
    is_registration = models.BooleanField(null=True, default=False)
    
    def __str__(self):
        return self.semester_id