from django.db import models
from Student.models import Student
from Databases.models import Subject, Semester

class RegistrationCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
