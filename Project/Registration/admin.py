from django.contrib import admin
from .models import RegistrationCourse
from Course.models import Course

def create_course(modeladmin, request, queryset):
    # Lấy tất cả các đăng ký được chọn
    registrations = queryset.all()

    # Lấy môn học của đăng ký đầu tiên để tạo lớp học mới
    first_registration = registrations.first()
    subject = first_registration.subject

    # Tạo một lớp học mới với môn học tương ứng
    course = Course.objects.create(name=f"{subject.name} Class", subject=subject)

    # Gắn các sinh viên từ các đăng ký đã chọn vào lớp học mới
    for registration in registrations:
        course.students.add(registration.student)

    # Lưu thay đổi
    course.save()

create_course.short_description = "Create Course from Registrations"

class RegistrationCourseAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject']
    actions = [create_course]

admin.site.register(RegistrationCourse, RegistrationCourseAdmin)
