from django.shortcuts import render
from django.views import View
from Course.models import Course
# Create your views here.

class CourseStudent(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        context = {
            "course": course
        }
        return render(request, "Course/course_student.html", context)
    
class CourseTeacher(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        context = {
            "course": course
        }
        return render(request, "Course/course_teacher.html", context)