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
        if start_hour is not None and subject is not None:
            hours = subject.hours
            end_hour = start_hour.hour + hours  # Accessing the hour attribute
            if end_hour > 18:
                raise forms.ValidationError(f"Thời gian học vượt quá 18 giờ. Hãy chọn lại giờ bắt đầu.")
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