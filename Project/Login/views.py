from django.shortcuts import render, HttpResponse
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
            return HttpResponse("Đăng nhập lỗi")
        else:
            login(request, myUser)
            if myUser.user_type == "Student":
                return HttpResponse("Đây là trang student")
            elif myUser.user_type == "Teacher":
                return HttpResponse("Đây là trang teacher")

