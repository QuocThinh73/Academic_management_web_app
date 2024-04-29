from django.db import models
from Student.models import Student
from Teacher.models import Teacher
from Databases.models import Subject, Semester

class Course(models.Model):
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject.name + " HK" + self.semester.semester_id