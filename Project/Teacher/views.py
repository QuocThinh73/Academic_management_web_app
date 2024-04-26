from django.shortcuts import render
from django.views import View

# Create your views here.

class TeacherView(View):
    def get(self, request):
        return render(request, "Teacher/teacher.html")