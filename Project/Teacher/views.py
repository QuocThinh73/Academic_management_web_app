from django.shortcuts import render, redirect
from django.views import View
from Course.models import Course

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
    
class UploadView(View):
    def get(self, request):
        return render(request, "Teacher/upload.html")
    
