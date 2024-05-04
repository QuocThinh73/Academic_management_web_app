from django.db import models
from Course.models import Course
# Create your models here.

class DayOfWeek(models.Model):
    day = models.CharField(max_length=3, unique=True) # Từ thứ 2 đến thứ 7

    def __str__(self):
        return self.day
    
class HourOfDay(models.Model):
    hour = models.IntegerField(unique=True) # Từ 7h đến 15h

    def __str__(self):
        return str(self.hour)

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    days = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE, null=True)
    start_hour = models.ForeignKey(HourOfDay, on_delete=models.CASCADE, null=True)
    end_hour = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.start_hour:
            self.end_hour = self.start_hour.hour + self.course.subject.hours
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.days} - {self.start_hour} - {self.start_hour.hour + self.course.subject.hours}"