from django.db import models
from Student.models import Student
from Databases.models import Subject

class RegistrationCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject.name
