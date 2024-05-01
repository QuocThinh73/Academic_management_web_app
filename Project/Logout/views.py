from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View
# Create your views here.

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("Login:home")