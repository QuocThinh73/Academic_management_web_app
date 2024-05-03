from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from Course.models import Course
from django.views import View
from Login.mixins import RoleRequiredMixin
# Create your views here.
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
            Document.course = course
            Document.description = form.cleaned_data.get('description')
            Document.syllabus = form.cleaned_data.get('syllabus')
            Document.course_file = form.cleaned_data.get('course_file')
            print("luu thanh cong")
            course.save()
        return redirect("File_document:AddDescription", course_id=course_id)