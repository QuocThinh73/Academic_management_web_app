from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "login/home.html")
    
class LoginView(View):
    def get(self, request):
        return render(request, "login/login.html")
    
    def post(self, request):
        tenDangNhap = request.POST.get('username')
        matKhau = request.POST.get('password')
        myUser = authenticate(username=tenDangNhap, password=matKhau)
        if myUser is None:
            return render(request, 'login/login_fail.html')
        else:
            login(request, myUser)
            if hasattr(myUser, "user_type"):
                if myUser.user_type == "Student":
                    return render(request, "login/home.html")
                elif myUser.user_type == "Teacher":
                    return render(request, "login/home.html")
            else:
                return redirect("admin:index")

