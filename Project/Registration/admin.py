from django.contrib import admin
from .models import RegistrationCourse
from Course.models import Course

def create_course(modeladmin, request, queryset):
    registrations = queryset.all()
    
    # Kiểm tra
    unique_subjects = set()
    for registration in registrations:
        unique_subjects.add(registration.subject)
    
    if len(unique_subjects) > 1:
        modeladmin.message_user(request, "Chỉ có thể chọn các đăng ký cùng một môn học để tạo lớp.", level='ERROR')
        return
    
    first_registration = registrations.first()
    subject = first_registration.subject
    semester = first_registration.semester
    num_courses = Course.count_courses_upon_subject(subject, semester)
    # Tạo lớp mới
    course = Course.objects.create(subject=subject, semester=semester, id_course=num_courses + 1)

    # Thêm sinh viên đã đăng kí môn vào lớp
    for registration in registrations:
        course.students.add(registration.student)

    course.save()

    # Xóa các đơn đăng ký sau khi tạo lớp thành công
    registrations.delete()
    modeladmin.message_user(request, "Đã tạo lớp học thành công.", level='SUCCESS')

create_course.short_description = "Tạo lớp học"

class RegistrationCourseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'student', 'semester']
    actions = [create_course]

admin.site.register(RegistrationCourse, RegistrationCourseAdmin)
