from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from .forms import DocumentFormSet
from Course.models import Course
from django.views import View
from Login.mixins import RoleRequiredMixin
# Create your views here.
class AddDescription(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        formset = DocumentFormSet(queryset=Document.objects.filter(course=course))
        return render(request, "Course/CourseTeacher/course_info.html",  {'formset': formset, 'course': course})
    
    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        formset = DocumentFormSet(request.POST, request.FILES, queryset=Document.objects.filter(course=course))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.course = course
                instance.save()
            formset.save_m2m()
            return redirect("File_document:AddDescription", course_id=course_id)
        return render(request, "Course/CourseTeacher/course_info.html",  {'formset': formset, 'course': course})