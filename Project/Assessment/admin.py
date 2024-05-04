from django.contrib import admin
from .models import TeacherAssessment, StudentAssessment

# Register your models here.
admin.site.register(TeacherAssessment)
admin.site.register(StudentAssessment)