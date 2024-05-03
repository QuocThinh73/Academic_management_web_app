from django.shortcuts import render, redirect
from .models import TeacherAssessment
from .forms import TeacherAssessmentForm
from django.views import View
from Login.mixins import RoleRequiredMixin
from django.views.generic import DetailView

# Create your views here.

#Hien trang de giao vien co the vo danh gia cho 1 sinh vien bat ky
class TeacherAssessmentView(RoleRequiredMixin, View):
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
class StudentAssessView(DetailView):
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
