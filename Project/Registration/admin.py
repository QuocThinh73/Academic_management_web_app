from django.contrib import admin
from .models import RegistrationCourse
from Course.models import Course
from Grade.models import Grade
from django.db.models import Count

class RegistrationCourseAdmin(admin.ModelAdmin):
    def create_course(modeladmin, request, queryset):
        # Group registrations by subject
        subject_groups = queryset.values('subject').annotate(total=Count('id')).order_by()

        # Iterate through each group of subjects
        for subject_group in subject_groups:
            subject_id = subject_group['subject']
            registrations = queryset.filter(subject_id=subject_id).order_by('id')

            # Calculate the number of courses needed based on a maximum of 5 students per course
            total_registrations = registrations.count()
            num_courses = (total_registrations + 4) // 5  # Adjusted to group by 5

            for course_number in range(num_courses):
                # Slice the queryset to handle only up to 5 registrations at a time
                start_index = course_number * 5
                end_index = start_index + 5
                current_registrations = registrations[start_index:end_index]

                if current_registrations.exists():
                    first_registration = current_registrations.first()
                    subject = first_registration.subject
                    semester = first_registration.semester
                    
                    # Count the existing courses for this subject and semester to generate the next course ID
                    existing_courses = Course.objects.filter(subject=subject, semester=semester).count()
                    course = Course.objects.create(
                        subject=subject,
                        semester=semester,
                        id_course=str(existing_courses + 1)
                    )
                    
                    # Add registered students to the new course
                    for registration in current_registrations:
                        course.students.add(registration.student)
                    
                    course.save()

                    # Create Grade records to manage scores
                    for registration in current_registrations:
                        grade = Grade.objects.create(student=registration.student, course=course)
                        grade.save()

                        # Delete registration individually
                        registration.delete()
        
        modeladmin.message_user(request, "Các lớp học đã được tạo thành công.", level='SUCCESS')

    create_course.short_description = "Tạo lớp học dựa trên môn đã chọn"

    list_display = ['subject', 'student', 'semester']
    list_filter = ['semester__semester_id', 'subject', 'student']
    actions = [create_course]

admin.site.register(RegistrationCourse, RegistrationCourseAdmin)
