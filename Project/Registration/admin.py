from django.contrib import admin
from .models import RegistrationCourse
from Course.models import Course
from Grade.models import Grade
from django.db.models import Count

class RegistrationCourseAdmin(admin.ModelAdmin):
    def create_course(modeladmin, request, queryset):
        subjects = queryset.values_list('subject', flat=True).distinct()
        
        for subject_id in subjects:
            all_registrations = RegistrationCourse.objects.filter(subject_id=subject_id).order_by('id')
            total_registrations = all_registrations.count()
            num_courses = (total_registrations + 4) // 5

            for course_number in range(num_courses):
                start_index = course_number * 5
                end_index = start_index + 5
                current_registrations = all_registrations[start_index:end_index]

                if current_registrations.exists():
                    first_registration = current_registrations.first()
                    subject = first_registration.subject
                    semester = first_registration.semester
                    
                    existing_courses = Course.objects.filter(subject=subject, semester=semester).count()
                    course = Course.objects.create(
                        subject=subject,
                        semester=semester,
                        id_course=str(existing_courses + 1)
                    )
                    
                    for registration in current_registrations:
                        course.students.add(registration.student)
                    
                    course.save()

                    for registration in current_registrations:
                        grade = Grade.objects.create(student=registration.student, course=course)
                        grade.save()
                        registration.delete()

        modeladmin.message_user(request, "Các lớp học đã được tạo thành công.", level='SUCCESS')

    create_course.short_description = "Tạo lớp học"

    list_display = ['subject', 'student', 'semester']
    list_filter = ['semester__semester_id', 'subject', 'student']
    actions = [create_course]

admin.site.register(RegistrationCourse, RegistrationCourseAdmin)
