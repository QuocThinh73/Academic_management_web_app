from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Teacher)

class DegreesAdmin(admin.ModelAdmin):
    list_display = ['teacher', '__str__']

admin.site.register(Degrees, DegreesAdmin)