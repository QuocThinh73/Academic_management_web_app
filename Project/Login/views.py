from django.shortcuts import render, redirect, HttpResponse
from django.views import View
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
            return render(request, "Login/login_fail.html")
        else:
            login(request, myUser)
            if myUser.user_type == "Student":
                return redirect("Student:student")
            elif myUser.user_type == "Teacher":
                return redirect("Teacher:teacher")

