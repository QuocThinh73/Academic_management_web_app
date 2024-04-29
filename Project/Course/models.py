from django.db import models
from Student.models import Student
from Teacher.models import Teacher
from Databases.models import Subject

class Course(models.Model):
    name = models.CharField(max_length=50, null=True, default="")
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name