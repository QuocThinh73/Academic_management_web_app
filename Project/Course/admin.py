from django.contrib import admin
from .models import *
from Schedule.models import Schedule
from django import forms
# Register your models here.

class ScheduleInlineForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        start_hour = cleaned_data.get('start_hour')
        subject = cleaned_data.get('course').subject
        days = cleaned_data.get('days')
        
        if start_hour and subject and days:
            end_hour = start_hour.hour + subject.hours

            if end_hour > 18:
                raise forms.ValidationError(f"Thời gian học vượt quá 18 giờ.")

            course = cleaned_data.get('course')

            teacher_schedules = Schedule.objects.filter(course__teacher=course.teacher, course__semester=course.semester, days=days).exclude(id=self.instance.id)
            for teacher_schedule in teacher_schedules:
                if (start_hour.hour >= teacher_schedule.start_hour.hour and start_hour.hour < teacher_schedule.end_hour) or (end_hour > teacher_schedule.start_hour.hour and end_hour <= teacher_schedule.end_hour):
                    raise forms.ValidationError(f"Trùng lịch với giảng viên.")
            
            students = course.students.all()
            for student in students:
                student_courses = student.course_set.all()
                for course in student_courses:
                    student_schedules = course.schedule_set.filter(course__semester=course.semester, days=days).exclude(id=self.instance.id)
                    print(f"{student.name}: {student_schedules}")

        return cleaned_data
    
class ScheduleInline(admin.TabularInline):
    model = Schedule
    can_delete = False
    form = ScheduleInlineForm

class CourseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'semester', 'id_course', 'teacher']
    list_filter = ['semester__semester_id', 'subject__name', 'students', 'teacher']
    inlines = [ScheduleInline]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, ScheduleInline) and obj:
                days = obj.subject.days
                ScheduleInline.extra = days
                ScheduleInline.max_num = days
                ScheduleInline.min_num = days
        return super().get_formsets_with_inlines(request, obj)

admin.site.register(Course, CourseAdmin)