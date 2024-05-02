from django import forms
from .models import TeacherAssessment

class TeacherAssessmentForm(forms.ModelForm):
    class Meta:
        model = TeacherAssessment
        fields = ['course', 'student', 'teacher', 'grade', 'comment']
from .models import Course

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['description', 'syllabus', 'course_file']
