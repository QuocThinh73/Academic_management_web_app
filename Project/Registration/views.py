from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from .models import RegistrationCourse
from Databases.models import Semester
from Login.mixins import RoleRequiredMixin
from django.contrib import messages
# Create your views here.

class RegistrationStudent(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request):
        current_semester = Semester.objects.filter(is_registration=True).first()
        form = RegistrationForm(initial={'semester': current_semester})
        context = {
            "form": form,
        }
        return render(request, "Registration/course_registration.html", context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Kiểm tra xem kỳ đăng ký có đúng là kỳ hiện tại không
            current_semester = Semester.objects.filter(is_registration=True).first()
            if form.cleaned_data['semester'] != current_semester:
                # Nếu không phải kỳ hiện tại, không cho phép đăng ký
                messages.error(request, f"Không thể đăng ký học kì {form.cleaned_data['semester']}. Chỉ có thể đăng kí học kì {current_semester}.")
                return redirect("Registration:registration_student")
            
            # Lấy dữ liệu từ form
            subject_id = form.cleaned_data['subject']
            student = request.user.student

            # Kiểm tra xem sinh viên đã đăng kí môn học này chưa
            if not RegistrationCourse.objects.filter(student=student, subject_id=subject_id).exists():
                registration = form.save(commit=False)
                registration.student = student
                registration.save()
                messages.success(request, f"Đăng kí môn {form.cleaned_data['subject']} thành công.")
                return redirect("Registration:registration_student")
            else:
                messages.error(request, f"Bạn đã đăng kí môn {form.cleaned_data['subject']}.")
                return redirect("Registration:registration_student")

        # Nếu form không hợp lệ hoặc sinh viên đã đăng kí môn học, hiển thị lại form
        return redirect("Registration:registration_student")