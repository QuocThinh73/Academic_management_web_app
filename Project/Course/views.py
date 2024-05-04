from django.shortcuts import render, redirect
from django.views import View
from Course.models import Course
from Grade.models import Grade
from File_document.models import Document
from Login.mixins import RoleRequiredMixin
from django.views.generic import ListView

class CourseTeacher(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        context = {
            "course": course,
        }
        return render(request, "Course/course_teacher.html", context)
    
class ListOfStudent(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        students = course.students.all()
        context = {
            "course": course,
            "students": students,
        }
        return render(request, "Course/CourseTeacher/list_of_student.html", context)
    
class Assessment(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'

    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        students = course.students.all()
        context = {
            "course": course,
            "students": students,
        }
        return render(request, "Course/CourseTeacher/assessment.html", context)
    
class CourseStudent(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'

    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        context = {
            "course": course
        }
        return render(request, "Course/course_student.html", context)

class ScoreView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        student = request.user.student
        grade = Grade.objects.filter(course=course, student=student).first()
        context = {
            "course": course,
            "student": student,
            "grade": grade,
        }
        return render(request, "Course/CourseStudent/ScoreView.html", context)
    
class DocumentView(RoleRequiredMixin, ListView):
    model = Document
    template_name = 'Course/CourseStudent/DocumentView.html'
    context_object_name = 'documents'

    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return Document.objects.filter(course__id=course_id)