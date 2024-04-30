from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from .models import RegistrationCourse
from Databases.models import Semester
# Create your views here.

class RegistrationStudent(View):
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
                return redirect("Registration:registration_student")
            
            # Lấy dữ liệu từ form
            subject_id = form.cleaned_data['subject']
            student = request.user.student

            # Kiểm tra xem sinh viên đã đăng kí môn học này chưa
            if not RegistrationCourse.objects.filter(student=student, subject_id=subject_id).exists():
                registration = form.save(commit=False)
                registration.student = student
                registration.save()
                return redirect("Registration:registration_student")

        # Nếu form không hợp lệ hoặc sinh viên đã đăng kí môn học, hiển thị lại form
        return render(request, 'Registration/course_registration.html', {'form': form})