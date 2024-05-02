from django.contrib import admin
from .models import Grade
# Register your models here.

class GradeAdmin(admin.ModelAdmin):
    list_filter = ['course__semester__semester_id', 'student__name']

admin.site.register(Grade, GradeAdmin)