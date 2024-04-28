from django.shortcuts import render
from django.views import View

# Create your views here.

class TeacherView(View):
    def get(self, request):
        return render(request, "teacher/teacher.html")

class AssessmentView(View):
    def get(self, request):
        return render(request, "teacher/assessment.html")

class ClassManageView(View):
    def get(self, request):
        return render(request, "teacher/class_manage.html")
    
class ImportScoreView(View):
    def get(self, request):
        return render(request, "teacher/import_score.html")
    
class UploadView(View):
    def get(self, request):
        return render(request, "teacher/upload.html")
    
