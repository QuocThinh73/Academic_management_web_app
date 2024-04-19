from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "Login/home.html")
    
class LoginView(View):
    def get(self, request):
        return render(request, "Login/login.html")
    
    def post(self, request):
        tenDangNhap = request.POST.get('username')
        matKhau = request.POST.get('password')
        myUser = authenticate(username=tenDangNhap, password=matKhau)
        if myUser is None:
            return render(request, 'Login/login_fail.html')
        else:
            login(request, myUser)
            if myUser.user_type == "Student":
                return HttpResponse("Đây là trang student")
            elif myUser.user_type == "Teacher":
                return HttpResponse("Đây là trang teacher")

