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
    description = models.TextField(null = True)
    syllabus = models.TextField(null = True)
    course_file = models.FileField(upload_to='Course/course_file/', null = True, blank=None)
    
    @classmethod
    def count_courses_upon_subject(cls, subject, semester):
        return cls.objects.filter(subject=subject, semester=semester).count()

    def __str__(self):
        name = self.subject.name + " HK" + self.semester.semester_id + " " + self.id_course
        return name

    
        