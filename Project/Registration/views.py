from django.shortcuts import render
from django.views import View
# Create your views here.

class RegistrationStudent(View):
    def get(self, request):
        return render(request, "Registration/course_registration.html")