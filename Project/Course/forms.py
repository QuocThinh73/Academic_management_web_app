from django import forms
from .models import TeacherAssessment
class TeacherAssessmentForm(forms.ModelForm):
    class Meta:
        model = TeacherAssessment
        fields = ['course', 'student', 'teacher', 'grade', 'comment']
