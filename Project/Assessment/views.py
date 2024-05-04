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
class StudentAssessView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        student = request.user.student
        assessment = TeacherAssessment.objects.filter(course=course, student=student).first()
        form = TeacherAssessmentForm(instance=assessment)
        context = {
            "course": course,
            "student": student,
            "assessment": assessment,
            "form": form,
        }
        return render(request, "Course/CourseStudent/student_receive_assess.html", context)
    
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
class TeacherAssessView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        teacher = request.user.teacher
        assessment = StudentAssessment.objects.filter(course=course).first()
        form = StudentAssessmentForm(instance=assessment)
        context = {
            "course": course,
            "assessment": assessment,
            "form": form,
        }
        return render(request, "Course/CourseTeacher/teacher_receive_assess.html", context)