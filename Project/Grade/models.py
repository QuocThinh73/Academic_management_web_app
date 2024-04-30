from django.db import models
from Student.models import Student
from Teacher.models import Teacher
from Course.models import Course

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    assignment_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    midterm_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    final_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        name = self.course.subject.name + " HK" + self.course.semester.semester_id
        return f"{self.student.name} - {name}"
