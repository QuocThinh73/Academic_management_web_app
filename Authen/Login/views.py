from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
class IndexClass(View):
    def get(self, request):
        return render(request, 'Home/index.html')
    
class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')
    
    def post(self, request):
        tendangnhap = request.POST.get('username')
        matkhau = request.POST.get('password')
        my_user = authenticate(username=tendangnhap, password=matkhau)
        if my_user is None:
            return render(request, 'Login/login_fail.html')
        login(request, my_user)
        return render(request, 'Student/student.html')
    
class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('Bạn vui lòng đăng nhập')
        else:
            return HttpResponse('Đây là ViewUser')