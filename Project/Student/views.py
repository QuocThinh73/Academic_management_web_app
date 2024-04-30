from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from Course.models import Course
from Grade.models import Grade
from django.contrib.auth.mixins import LoginRequiredMixin

class StudentView(View):
    def get(self, request):
        return render(request, "Student/student.html")
    
class StudentCourse(View):
    def get(self, request):
        # Lấy thông tin sinh viên
        student = request.user.student
        student_courses = Course.objects.filter(students=student)

        # Sắp xếp lớp học theo kì để hiển thị
        courses_by_semester = {}
        for course in student_courses:
            semester_id = course.semester.semester_id
            if semester_id not in courses_by_semester:
                courses_by_semester[semester_id] = []
            courses_by_semester[semester_id].append(course)
        courses_by_semester = dict(sorted(courses_by_semester.items(), reverse=True))

        context = {
            'courses_by_semester': courses_by_semester,
        }
        return render(request, "Student/my_course.html", context)
    
class StudentProfile(View):
    def get(self, request):
        # Lấy thông tin của sinh viên
        student = request.user.student
        student_email = request.user.email
        grades = Grade.objects.filter(student=student)

        # Sắp xếp lại điểm theo kì để hiển thị
        grades_by_semester = {}
        for grade in grades:
            semester_id = grade.course.semester.semester_id
            if semester_id not in grades_by_semester:
                grades_by_semester[semester_id] = []
            grades_by_semester[semester_id].append(grade)
        grades_by_semester = dict(sorted(grades_by_semester.items(), reverse=True))

        context = {
                "student" : student,
                "student_email" : student_email,
                "grades_by_semester": grades_by_semester,
        }
        return render(request, "Student/profile.html", context)