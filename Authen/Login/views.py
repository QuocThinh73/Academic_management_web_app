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
        return HttpResponse('Bạn vừa bấm đăng nhập')