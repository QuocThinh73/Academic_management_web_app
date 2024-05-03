from django.shortcuts import render
from django.views import View
from Course.models import Course
from .models import *
from Login.mixins import RoleRequiredMixin

# Create your views here.

class TeacherView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request):
        return render(request, "Teacher/teacher.html")

class ClassManageView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request):
        teacher = request.user.teacher
        courses = Course.objects.filter(teacher=teacher)
        context = {
            "courses": courses
        }
        return render(request, "Teacher/class_manage.html", context)
    
class TeacherProfile(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'

    def get(self, request):
        #Lay thong tin giao vien
        teacher = request.user.teacher
        teacher_mail = request.user.email
        degrees = Degrees.objects.filter(teacher=teacher)
        department = teacher.department

        #Hien thi thong tin giao vien
        context = {
            'teacher': teacher,
            'teacher_mail': teacher_mail,
            'degrees': degrees,
            'department': department,
        }
        return render(request, 'Teacher/teacher_profile.html', context)

        


    
