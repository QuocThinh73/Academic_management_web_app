from django.shortcuts import render, redirect
from django.views import View
from Course.models import Course
from Grade.models import Grade
from Login.mixins import RoleRequiredMixin
from .forms import DocumentForm

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
    
<<<<<<< HEAD
class AddDescription(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        form = DocumentForm(prefix = course_id)
        context = {
        "course": course,
        "form": form,
        }
        return render(request, "Course/CourseTeacher/course_info.html", context)
    
    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        form = DocumentForm(request.POST, prefix=course_id)
        if form.is_valid():
            #course, created = Course.objects.get_or_create()
            course.description = form.cleaned_data.get('description')
            course.syllabus = form.cleaned_data.get('syllabus')
            course.course_file = form.cleaned_data.get('course_file')
            course.save()
        return redirect("Course:AddDescription", course_id=course_id)
=======
class Assessment(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'

    def get(self, request, course_id):
        return render(request, "Course/CourseTeacher/assessment.html")
    
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
    
class DocumentView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request, course_id):
        context = {

        }
        return render(request, "Course/CourseStudent/DocumentView.html", context)

>>>>>>> 37ad29e0d6f58bd500e8b7ce7116c056aead57ab
