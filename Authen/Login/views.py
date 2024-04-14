from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate

# Create your views here.
class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Xin chào</h1>')
    
class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')
    
    def post(self, request):
        tendangnhap = request.POST.get('username')
        matkhau = request.POST.get('password')
        my_user = authenticate(username=tendangnhap, password=matkhau)
        if my_user is None:
            return HttpResponse('User không tồn tại')
        return HttpResponse('Bạn vừa bấm đăng nhập %s %s'%(tendangnhap, matkhau))