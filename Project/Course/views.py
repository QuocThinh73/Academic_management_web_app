from django.shortcuts import render, HttpResponse
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
            "course": course,
        }
        return render(request, "Course/course_teacher.html", context)
    
class ListOfStudent(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        students = course.students.all()
        context = {
            "course": course,
            "students": students,
        }
        return render(request, "Course/list_of_student.html", context)

class ImportScore(View):
    def get(self, request, course_id):
        return HttpResponse("Nhập điểm")