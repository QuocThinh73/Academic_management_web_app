from django.db import models
from Course.models import Course
from Student.models import Student
from Teacher.models import Teacher
from Grade.models import Grade

# Create your models here.

#Teacher danh gia Student  
class TeacherAssessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    comment = models.TextField()

    class Meta:
        unique_together = ('course', 'student', 'teacher')

    def get_average_grade(self):
        return self.grade.average_score
    
    def get_letter_grade(self):
        average_score = self.get_average_grade()
        if average_score >= 9.0:
            return 'A'
        elif average_score >= 8.0:
            return 'B'
        elif average_score >= 7.0:
            return 'C'
        elif average_score >= 6.0:
            return 'D'
        else:
            return 'F'
        
#Student danh gia Teacher
class StudentAssessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    course_feedback = models.TextField()
    teacher_feedback = models.TextField()
    improvements = models.TextField()
    
    def __str__(self):
        return f'Review for {self.course}'


