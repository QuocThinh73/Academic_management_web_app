from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms

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
    
class ViewUser(LoginRequiredMixin, View):
    login_url = '/Login/'
    def get(self, request):
        return HttpResponse('Đây là ViewUser')

@decorators.login_required(login_url='/Login/')
def view_score(request):
    return HttpResponse('Đây là view score')

class AddPost(LoginRequiredMixin, View):
    login_url = '/Login/'
    def get(self, request):
        f = forms.PostForm()
        context = {'fm' : f}
        return render(request, 'Login/add_post.html', context)
    
    def post(self, request):
        f = forms.PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('Nhập sai dữ liệu rồi')
        print(request.user.get_all_permissions())
        if request.user.has_perm('Login.add_post'):
            f.save()
        else:
            return HttpResponse('Không có quyền')
        return HttpResponse('Đã thêm')