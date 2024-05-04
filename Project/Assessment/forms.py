from django import forms
from .models import TeacherAssessment, StudentAssessment

class TeacherAssessmentForm(forms.ModelForm):
    class Meta:
        model = TeacherAssessment
        fields = ['comment']

class StudentAssessmentForm(forms.ModelForm):
    class Meta:
        model = StudentAssessment
        fields = ['course_feedback', 'teacher_feedback', 'improvements']
        widgets = {
            'course_feedback': forms.Textarea(attrs={'placeholder': 'Your feedback about the course'}),
            'teacher_feedback': forms.Textarea(attrs={'placeholder': 'Your feedback about the teacher'}),
            'improvements': forms.Textarea(attrs={'placeholder': 'What could be improved?'}),
        }