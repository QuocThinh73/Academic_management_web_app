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
        documents = Document.objects.filter(course = course)
        form = DocumentForm( instance=documents)
        context = {
        "course": course,
        "form": form,
        }
        return render(request, "Course/CourseTeacher/course_info.html", context)
    
    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        form = DocumentForm(request.POST, prefix=course_id)
        if form.is_valid():
            document, created = Document.objects.get_or_create(course = course)
            if created is False:
                document.description = form.cleaned_data.get('description')
                document.syllabus = form.cleaned_data.get('syllabus')
                document.course_file = form.cleaned_data.get('course_file')
                document.save()
        return redirect("File_document:AddDescription", course_id=course_id)