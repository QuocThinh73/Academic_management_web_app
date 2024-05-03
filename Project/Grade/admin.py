from django.contrib import admin
from .models import Grade
# Register your models here.

class GradeAdmin(admin.ModelAdmin):
    list_filter = ['course__semester__semester_id', 'student__name']
    list_display = ['__str__', 'assignment_score', 'midterm_score', 'final_score']

admin.site.register(Grade, GradeAdmin)