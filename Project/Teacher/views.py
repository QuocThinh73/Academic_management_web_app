from django.shortcuts import render, redirect
from django.views import View
from Course.models import Course
from .models import *

# Create your views here.

class TeacherView(View):
    def get(self, request):
        return render(request, "Teacher/teacher.html")

class AssessmentView(View):
    def get(self, request):
        return render(request, "Teacher/assessment.html")

class ClassManageView(View):
    def get(self, request):
        teacher = request.user.teacher
        courses = Course.objects.filter(teacher=teacher)
        context = {
            "courses": courses
        }
        return render(request, "Teacher/class_manage.html", context)
    
class ImportScoreView(View):
    def get(self, request):
        return redirect("Grade:")
    
class UploadView(View):
    def get(self, request):
        return render(request, "Teacher/upload.html")
    
class TeacherProfile(View):
    def get(self, request):
        #Lay thong tin giao vien
        teacher = request.user.teacher
        teacher_mail = request.user.email
        degrees = Degrees.objects.filter(teacher=teacher)
        department = teacher.department
        teaching_schedule = teacher.teaching_schedule

        #Hien thi thong tin giao vien
        context = {
            'teacher': teacher,
            'teacher_mail': teacher_mail,
            'degrees': degrees,
            'department': department,
            'teaching_schedule': teaching_schedule,
        }
        return render(request, 'Teacher/teacher_profile.html', context)

        


    
