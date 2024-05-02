from django.db import models
from Course.models import Course
# Create your models here.

class DayOfWeek(models.Model):
    day = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.day
class HourOfDay(models.Model):
    hour = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.hour)

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    days = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE, null=True)
    hours = models.ForeignKey(HourOfDay, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.course