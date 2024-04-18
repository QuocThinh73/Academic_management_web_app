from django.contrib import admin
from . import models
from .models import *

admin.site.register(MyUser)
# Register your models here.
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'student_id', 'score', 'date_of_birth', 'major', 'enrollment_date']

admin.site.register(StudentUser, StudentUserAdmin)

class TeacherUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'teacher_id']

admin.site.register(TeacherUser, TeacherUserAdmin)