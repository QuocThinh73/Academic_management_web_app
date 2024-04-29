from django.contrib import admin
from .models import RegistrationCourse
from Course.models import Course

def create_course(modeladmin, request, queryset):
    registrations = queryset.all()

    # Kiểm tra
    unique_subjects = registrations.values_list('subject', flat=True).distinct()
    if len(unique_subjects) > 1:
        modeladmin.message_user(request, "Chỉ có thể chọn các đăng ký cùng một môn học để tạo lớp.", level='ERROR')
        return
    
    first_registration = registrations.first()
    subject = first_registration.subject

    # Tạo lớp mới
    course = Course.objects.create(name=f"{subject.name} Class", subject=subject)

    # Thêm sinh viên đã đăng kí môn vào lớp
    for registration in registrations:
        course.students.add(registration.student)

    course.save()

create_course.short_description = "Tạo lớp học"

class RegistrationCourseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'student']
    actions = [create_course]

admin.site.register(RegistrationCourse, RegistrationCourseAdmin)
