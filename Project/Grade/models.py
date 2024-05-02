from django.db import models
from Student.models import Student
from Course.models import Course

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    assignment_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    midterm_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    final_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    @property
    def average_score(self):
        if self.assignment_score is not None and self.midterm_score is not None and self.final_score is not None:
            assignment_score = float(self.assignment_score)
            midterm_score = float(self.midterm_score)
            final_score = float(self.final_score)
            return round((assignment_score * 0.2 + midterm_score * 0.3 + final_score * 0.5), 2)
        else:
            return None
    
    def __str__(self):
        name = self.course.subject.name + " HK" + self.course.semester.semester_id
        return f"{self.student.name} - {name}"
