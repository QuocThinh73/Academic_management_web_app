from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from Course.models import Course
from Grade.models import Grade
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
        grades = Grade.objects.filter(course=course)
        context = {
            "course": course,
            "students": students,
            "grades": grades,
        }
        return render(request, "Course/CourseTeacher/import_score.html", context)

    def post(self, request, course_id):
        course = Course.objects.get(pk=course_id)
        students = course.students.all()
        for student in students:
            assignment_score = request.POST.get(f'assignment_{student.id}')
            midterm_score = request.POST.get(f'midterm_{student.id}')
            final_score = request.POST.get(f'final_{student.id}')

            if assignment_score is not None and midterm_score is not None and final_score is not None:
                # Kiểm tra nếu giá trị có thể chuyển đổi thành số thực
                try:
                    assignment_score = float(assignment_score)
                    midterm_score = float(midterm_score)
                    final_score = float(final_score)
                except ValueError:
                    # Nếu không thể chuyển đổi thành số thực, bỏ qua và hiển thị thông báo lỗi
                    return HttpResponse("Invalid score values")

                # Truy vấn bản ghi Grade của sinh viên trong khóa học này
                grade, created = Grade.objects.get_or_create(
                    student=student,
                    course=course,
                    teacher=request.user.teacher  # Thay bằng user hiện tại
                )

                # Cập nhật điểm cho sinh viên
                grade.assignment_score = assignment_score
                grade.midterm_score = midterm_score
                grade.final_score = final_score
                grade.save()

        # Chuyển hướng hoặc hiển thị thông báo thành công nếu cần
        return HttpResponse("Scores saved successfully")