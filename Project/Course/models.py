from django.db import models
from Student.models import Student
from Teacher.models import Teacher
from Databases.models import Subject, Semester

class Course(models.Model):
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)
    id_course = models.CharField(max_length=3, null=True)

    @classmethod
    def count_courses_upon_subject(cls, subject, semester):
        return cls.objects.filter(subject=subject, semester=semester).count()

    def __str__(self):
        name = self.subject.name + " HK" + self.semester.semester_id + " " + self.id_course
        return name

#Teacher danh gia Student  
class TeacherAssessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    grade = models.ForeignKey('Grade.Grade', on_delete=models.CASCADE, null=True)
    comment = models.TextField()

    class Meta:
        unique_together = ('course', 'student', 'teacher')

    def get_rating(self):
        total_result = self.grade.final_score

        if total_result is None:
            return None
        elif total_result >= 9.5:
            return 'A+'
        elif total_result >= 8.5 and total_result < 9.5:
            return 'A'
        elif total_result >= 8.0 and total_result < 8.5:
            return 'B+'
        elif total_result >= 7.5 and total_result < 8.0:
            return 'B'
        elif total_result >= 7.0 and total_result < 7.5:
            return 'C+'
        elif total_result >= 6.5 and total_result < 7.0:
            return 'C'
        elif total_result >= 6.0 and total_result < 6.5:
            return 'D+'
        elif total_result >= 4.0 and total_result < 6.0:
            return 'D'
        else:
            return 'F'
        