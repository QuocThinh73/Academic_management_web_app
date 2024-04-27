from django.shortcuts import render
from django.views import View
from .models import Student
from Course.models import Course
from django.contrib.auth.mixins import LoginRequiredMixin

class StudentView(View):
    def get(self, request):
        return render(request, "Student/student.html")
    
class StudentCourse(View):
    def get(self, request):
        current_user = request.user
        student = Student.objects.get(username=current_user)
        student_courses = student.course_set.all()
        context = {
            'courses': student_courses,
        }
        return render(request, "Student/my_course.html", context)
    
class StudentProfile(View):
    def get(self, request):
        current_user = request.user
        student = Student.objects.get(username=current_user)
        student_email = current_user.email
        context = {
                "student" : student,
                "student_email" : student_email,
        }
        return render(request, "Student/profile.html", context)
    
class StudentRegister(View):
    def get(self, request):
        return render(request, "Student/course_registration.html")