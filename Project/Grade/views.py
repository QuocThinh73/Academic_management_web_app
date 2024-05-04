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
            form = GradeForm(prefix=student.student_id, instance=grade)
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
        forms = []
        form_is_valid = True

        for student in students:
            form = GradeForm(request.POST, prefix=student.student_id)
            if form.is_valid():
                grade, created = Grade.objects.get_or_create(student=student, course=course)
                if not created:
                    grade.assignment_score = form.cleaned_data.get('assignment_score')
                    grade.midterm_score = form.cleaned_data.get('midterm_score')
                    grade.final_score = form.cleaned_data.get('final_score')
                    grade.teacher = request.user.teacher
                    grade.save()
            else:
                form_is_valid = False
            forms.append((student, form))

        if form_is_valid:
            return redirect("Grade:ImportScore", course_id=course_id)
        else:
            # Re-render the page with the existing data to show errors
            context = {
                "course": course,
                "students": students,
                "forms": forms,
            }
        return render(request, "Course/CourseTeacher/import_score.html", context)