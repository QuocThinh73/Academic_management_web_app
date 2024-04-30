from django.contrib import admin
from .models import Grade
# Register your models here.

class GradeAdmin(admin.ModelAdmin):
    def add_teacher_to_grade(self, request, queryset):
        for grade in queryset:
            # Có giáo viên rồi thì bỏ qua
            if grade.teacher:
                continue

            # Tìm giáo viên quản lí course đó để thêm vào
            if grade.course.teacher:
                grade.teacher = grade.course.teacher
                grade.save()
                self.message_user(request, f"Đã thêm giáo viên cho {grade} thành công.", level='SUCCESS')
            else:
                self.message_user(request, f"Không tìm thấy giáo viên của {grade}.", level='WARNING')

            
    add_teacher_to_grade.short_description = "Thêm giáo viên"

    actions = ['add_teacher_to_grade']

admin.site.register(Grade, GradeAdmin)