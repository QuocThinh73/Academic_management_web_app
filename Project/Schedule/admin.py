from django.contrib import admin
from .models import Schedule, DayOfWeek, HourOfDay
# Register your models here.

admin.site.register(DayOfWeek)
admin.site.register(HourOfDay)
admin.site.register(Schedule)