from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Major)

class SemesterAdmin(admin.ModelAdmin):
    # Định nghĩa hành động tạo học kỳ mới
    def create_new_semester(self, request, queryset):
        # Lấy ra số kì cuối cùng
        last_semester = Semester.objects.order_by('-semester_id').first()
        if last_semester:
            # Tách chuỗi semester_id thành năm và số thứ tự kì
            year = int(last_semester.semester_id[:2])
            ordinal = int(last_semester.semester_id[2:]) + 1
            if ordinal > 3:
                ordinal = 1
                year += 1
            # Tạo semester_id mới
            new_semester_id = f"{year}{ordinal}"
        else:
            # Trường hợp không có kì nào trong database
            new_semester_id = "232"

        # Tạo học kỳ mới
        new_semester = Semester.objects.create(semester_id=new_semester_id, is_registration=True)

    # Thiết lập metadata cho action
    create_new_semester.short_description = "Tạo học kỳ mới"

    # Đăng ký action vào trang admin
    actions = [create_new_semester]

admin.site.register(Semester, SemesterAdmin)