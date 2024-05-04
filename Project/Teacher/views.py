from django.shortcuts import render
from django.views import View
from Course.models import Course
from .models import *
from Login.mixins import RoleRequiredMixin
from Schedule.models import Schedule
from collections import defaultdict

# Create your views here.

class TeacherView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request):
        return render(request, "Teacher/teacher.html")

class ClassManageView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request):
        teacher = request.user.teacher
        courses = Course.objects.filter(teacher=teacher)

        courses_by_semester = {}
        for course in courses:
            semester_id = course.semester.semester_id
            if semester_id not in courses_by_semester:
                courses_by_semester[semester_id] = []
            courses_by_semester[semester_id].append(course)
        courses_by_semester = dict(sorted(courses_by_semester.items(), reverse=True))


        context = {
            "courses_by_semester": courses_by_semester
        }
        return render(request, "Teacher/class_manage.html", context)
    
class TeacherProfile(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'

    def get(self, request):
        #Lay thong tin giao vien
        teacher = request.user.teacher
        teacher_mail = request.user.email
        degrees = Degrees.objects.filter(teacher=teacher)

        #Hien thi thong tin giao vien
        context = {
            'teacher': teacher,
            'teacher_mail': teacher_mail,
            'degrees': degrees,
        }
        return render(request, 'Teacher/teacher_profile.html', context)

class TeacherSchedule(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Teacher'
    
    def get(self, request):
        teacher = request.user.teacher
        techer_courses = Course.objects.filter(teacher=teacher)

        teacher_schedules = Schedule.objects.filter(course__in=techer_courses)
        schedules_by_semester = defaultdict(list)

        for schedule in teacher_schedules:
            semester_id = schedule.course.semester.semester_id
            schedules_by_semester[semester_id].append(schedule)

        schedules_by_semester = dict(sorted(schedules_by_semester.items(), reverse=True))
        days_order = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        for schedules in schedules_by_semester.values():
            schedules.sort(key=lambda x: (days_order.index(x.days.day), x.start_hour.hour))

        context = {
            "schedules_by_semester": schedules_by_semester
        }

        return render(request, "Teacher/schedule_view.html", context)


    
