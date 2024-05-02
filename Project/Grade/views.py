from django.shortcuts import render, redirect
from .models import Grade
from .forms import GradeForm
from Course.models import Course
from django.views import View
from Login.mixins import RoleRequiredMixin

class ImportScore(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        students = course.students.all()
        forms = []
        for student in students:
            grade = Grade.objects.filter(student=student, course=course).first()
            form = GradeForm(prefix=student.id, instance=grade)
            forms.append((student, form))

        context = {
            "course": course,
            "students": students,
            "forms": forms,
        }

        return render(request, "Course/CourseTeacher/import_score.html", context)

    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        students = course.students.all()
        for student in students:
            form = GradeForm(request.POST, prefix=student.id)
            if form.is_valid():
                # Kiểm tra xem có bản ghi Grade của sinh viên trong khóa học này không
                grade, created = Grade.objects.get_or_create(student=student, course=course)
                # Cập nhật điểm
                if created is False:
                    grade.assignment_score = form.cleaned_data.get('assignment_score')
                    grade.midterm_score = form.cleaned_data.get('midterm_score')
                    grade.final_score = form.cleaned_data.get('final_score')
                    grade.teacher = request.user.teacher
                    grade.save()

        return redirect("Grade:ImportScore", course_id=course_id)