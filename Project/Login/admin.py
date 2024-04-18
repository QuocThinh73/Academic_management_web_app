from django.contrib import admin
from . import models
from .models import MyUser

# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type']

admin.site.register(MyUser, MyUserAdmin)