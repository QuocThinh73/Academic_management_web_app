from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from Course.models import Course
from Grade.models import Grade
from Grade.forms import GradeForm
# Create your views here.

class CourseStudent(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        context = {
            "course": course
        }
        return render(request, "Course/course_student.html", context)
    
class CourseTeacher(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        context = {
            "course": course,
        }
        return render(request, "Course/course_teacher.html", context)
    
class ListOfStudent(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        students = course.students.all()
        context = {
            "course": course,
            "students": students,
        }
        return render(request, "Course/CourseTeacher/list_of_student.html", context)

class ImportScore(View):
    def get(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        students = course.students.all()
        forms = []
        for student in students:
            form = GradeForm(prefix=student.id)
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

        return redirect("Course:ImportScore", course_id=course_id)