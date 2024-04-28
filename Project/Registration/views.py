from django.shortcuts import render, redirect
from django.views import View
from Databases.models import Subject
from .forms import RegistrationForm
from .models import RegistrationCourse
# Create your views here.

class RegistrationStudent(View):
    def get(self, request):
        subjects = Subject.objects.all()
        form = RegistrationForm()
        context = {
            "form": form,
        }
        return render(request, "Registration/course_registration.html", context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            subject_id = form.cleaned_data['subject']
            student = request.user.student

            # Kiểm tra xem sinh viên đã đăng kí môn học này chưa
            if not RegistrationCourse.objects.filter(student=student, subject_id=subject_id).exists():
                # Nếu chưa đăng kí, lưu thông tin đăng kí vào database
                registration = form.save(commit=False)
                registration.student = student
                registration.save()
                return redirect("Registration:registration_student")

        # Nếu form không hợp lệ hoặc sinh viên đã đăng kí môn học, hiển thị lại form
        return render(request, 'Registration/course_registration.html', {'form': form})
