from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_login(request):
    return render(request, 'login/login.html')