from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Subject)
admin.site.register(Department)

class MajorAdmin(admin.ModelAdmin):
    list_filter = ["department"]

admin.site.register(Major, MajorAdmin)

class SemesterAdmin(admin.ModelAdmin):

    list_display = ["semester_id", "is_registration"]

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
        Semester.objects.create(semester_id=new_semester_id, is_registration=True)

    def set_registration(self, request, queryset):
        queryset.update(is_registration=False)
    
    create_new_semester.short_description = "Tạo học kỳ mới"
    set_registration.short_description = "Kết thúc học kỳ"

    actions = [create_new_semester, set_registration]

admin.site.register(Semester, SemesterAdmin)