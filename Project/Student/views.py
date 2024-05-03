from django.shortcuts import render
from django.views import View
from Course.models import Course
from Grade.models import Grade
from Schedule.models import Schedule
from Login.mixins import RoleRequiredMixin
from collections import defaultdict


class StudentView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request):
        return render(request, "Student/student.html")
    
class StudentCourse(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request):
        # Lấy thông tin sinh viên
        student = request.user.student
        student_courses = Course.objects.filter(students=student)

        # Sắp xếp lớp học theo kì để hiển thị
        courses_by_semester = {}
        for course in student_courses:
            semester_id = course.semester.semester_id
            if semester_id not in courses_by_semester:
                courses_by_semester[semester_id] = []
            courses_by_semester[semester_id].append(course)
        courses_by_semester = dict(sorted(courses_by_semester.items(), reverse=True))

        context = {
            'courses_by_semester': courses_by_semester,
        }
        return render(request, "Student/my_course.html", context)
    
class StudentProfile(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request):
        # Lấy thông tin của sinh viên
        student = request.user.student
        student_email = request.user.email

        context = {
            "student" : student,
            "student_email" : student_email,
        }
        return render(request, "Student/profile.html", context)
    
class ScoreView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    @classmethod
    def get_semester(cls, student):
        courses = Course.objects.filter(students=student)
        semesters = []
        for course in courses:
            semesters.append(course.semester.semester_id)
        unique_sorted_semesters = sorted(set(semesters))
        return unique_sorted_semesters

    @classmethod
    def get_info_by_semester(cls, student):
        info_by_semester = {}
        semesters = cls.get_semester(student=student)
        score = 0
        credit = 0
        for semester in semesters:
            grades_in_semester = Grade.objects.filter(student=student, course__semester__semester_id=semester)
            grades_info = []
            total_score = 0
            total_credit = 0

            for grade in grades_in_semester:
                if grade.average_score is not None:
                    total_score += grade.average_score * grade.course.subject.credit
                    total_credit += grade.course.subject.credit
                    score += grade.average_score * grade.course.subject.credit
                    credit += grade.course.subject.credit
                grades_info.append({
                    'subject': grade.course.subject.name,
                    'assignment_score': grade.assignment_score,
                    'midterm_score': grade.midterm_score,
                    'final_score': grade.final_score,
                    'average_score': grade.average_score
                })

            average_score_semester =  round(total_score / total_credit, 1) if total_credit > 0 else None
            average_score_all =  round(score / credit, 1) if credit > 0 else None

            info_by_semester[semester] = {
                'grades_info': grades_info,
                'average_score_semester': average_score_semester,
                'average_score_all': average_score_all,
                'credit': credit,
            }

        info_by_semester = {semester: info_by_semester[semester] for semester in sorted(info_by_semester.keys(), reverse=True)}
        
        return info_by_semester

    def get(self, request):
        # Lấy thông tin của sinh viên
        student = request.user.student
        info_by_semester = self.get_info_by_semester(student)

        context = {
            "info_by_semester": info_by_semester,
        }
    
        return render(request, "Student/score_view.html", context)
        

class ScheduleView(RoleRequiredMixin, View):
    def has_permission(self, user):
        return user.user_type == 'Student'
    
    def get(self, request):
        student = request.user.student
        student_courses = Course.objects.filter(students=student)

        student_schedules = Schedule.objects.filter(course__in=student_courses)
        schedules_by_semester = defaultdict(list)

        for schedule in student_schedules:
            semester_id = schedule.course.semester.semester_id
            schedules_by_semester[semester_id].append(schedule)

        schedules_by_semester = dict(sorted(schedules_by_semester.items(), reverse=True))
        days_order = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        for schedules in schedules_by_semester.values():
            schedules.sort(key=lambda x: (days_order.index(x.days.day), x.start_hour.hour))
        print(schedules_by_semester)

        context = {
            "schedules_by_semester": schedules_by_semester
        }

        return render(request, "Student/schedule_view.html", context)