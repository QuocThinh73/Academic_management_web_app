from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TeacherAssessment, StudentAssessment
from Course.models import Course
from Student.models import Student
from .forms import TeacherAssessmentForm, StudentAssessmentForm
from django.views import View
from Login.mixins import RoleRequiredMixin
from django.views.generic import DetailView

# Create your views here.

#Hien trang de giao vien co the vo danh gia cho 1 sinh vien bat ky
class TeacherAssessmentView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, course_id):
        form = TeacherAssessmentForm()
        course = Course.objects.get(id=course_id)
        students_course = course.students.all()
        context = {
            "form": form,
            "course": course,
            "students_course": students_course,
        }
        return render(request, "Course/CourseTeacher/teacher_assess.html", context)
    
    def post(self, request, course_id):
        course = Course.objects.get(id=course_id)
        students = course.students.all()
        for student in students:
            form = TeacherAssessmentForm(request.POST)
            if form.is_valid():
                assess, created = TeacherAssessment.objects.get_or_create(student=student, course=course)
                if created is False:
                    assess = form.save(commit=False)
                    assess.comment = form.cleaned_data['comment']
                    assess.save()
                    messages.success(request, 'Your assessment was saved')
                
        return redirect("Assessment:TeacherAssessmentView", course_id=course_id)

#Student xem danh gia tu giao vien
class StudentAssessView(DetailView):
    model = TeacherAssessment
    template_name = "Course/CourseStudent/student_receive_assess.html"
    context_object_name = "assessment"

    def get_queryset(self):
        return self.model.objects.filter(student_id=self.kwargs['pk'])

#Hien trang de sinh vien co the vo danh gia giao vien cho mon hoc tuong ung
class StudentAssessmentView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request, course_id):
        form = StudentAssessmentForm()
        course = Course.objects.get(id=course_id)
        context = {
            'form': form,
            'course': course,
        }
        return render(request, "Course/CourseStudent/student_assess.html", context)

    def post(self, request, course_id):
        course = Course.objects.get(id=course_id)
        students = course.students.all()
        for student in students:
            form = StudentAssessmentForm(request.POST)
            if form.is_valid():
                assessment, created = TeacherAssessment.objects.get_or_create(student=student, course=course)
                if created is False:
                    assessment = form.save(commit=False)
                    assessment.course_feedback = form.cleaned_data['course_feedback']
                    assessment.teacher_feedback = form.cleaned_data['teacher_feedback']
                    assessment.improvements = form.cleaned_data['improvements']
                    assessment.save()
                    messages.success(request, 'Your assessment was saved')
                
        return redirect("Assessment:StudentAssessmentView", course_id=course_id)
    
#Hien trang de giao vien coi danh gia tu sinh vien
class TeacherAssessView(DetailView):
    model = StudentAssessment
    template_name = "Course/CourseTeacher/teacher_receive_assess.html"
    context_object_name = "assessments"

    def get_queryset(self):
        return self.model.objects.filter(course_id=self.kwargs['course_id'])
