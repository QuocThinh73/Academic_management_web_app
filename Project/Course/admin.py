from django.contrib import admin
from .models import *
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['subject', 'semester', 'id_course', 'teacher']
    list_filter = ['semester__semester_id', 'subject__name', 'students', 'teacher']

admin.site.register(Course, CourseAdmin)