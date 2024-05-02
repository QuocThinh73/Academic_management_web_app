from django.shortcuts import render, redirect
from django.views import View
from Course.models import Course
from Grade.models import Grade
from Login.mixins import RoleRequiredMixin
from .forms import TeacherAssessmentForm
from django.views.generic.detail import DetailView
from .models import TeacherAssessment
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
    

#Hien trang danh gia sinh vien danh cho giao vien
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
    
class Assessment(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'

    def get(self, request, course_id):
        return render(request, "Course/CourseTeacher/assessment.html")
    
#Hien trang de giao vien co the vo danh gia cho 1 sinh vien bat ky
class TeacherAssessment(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, course_id, student_id):
        form = TeacherAssessmentForm()
        return render(request, "Course/CourseTeacher/teacher_assess.html", {"form": form})
    
    def post(self, request, course_id, student_id):
        form = TeacherAssessmentForm(request.POST)
        if form.is_valid():
            assess = form.save(commit=False)
            assess.course_id = course_id
            assess.teacher = request.user
            assess.student_id = student_id
            assess.save()
            return redirect('Course:assessment', course_id = course_id)
        return render(request, "Course/CourseTeacher/teacher_assess.html", {"form": form})

#Student xem danh gia tu giao vien
class StudentReceiveAssess(DetailView):
    model = TeacherAssessment
    template_name = "Course/CourseStudent/student_receive_assess.html"
    context_object_name = "assessment"

    def get_queryset(self):
        return self.model.objects.filter(student_id=self.kwargs['student_id'])

#Hien trang de sinh vien co the vo danh gia giao vien cho mon hoc tuong ung
class StudentAssessment(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request):
        pass

    
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


