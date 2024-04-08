from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"name": "Zack"}
    return render(request, "home.html", context)