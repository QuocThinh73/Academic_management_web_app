from django import forms
from .models import TeacherAssessment, StudentAssessment
from Student.models import Student
from Course.models import Course

class TeacherAssessmentForm(forms.ModelForm):
    student_id = forms.ModelChoiceField(queryset=Student.objects.all())
    class Meta:
        model = TeacherAssessment
        fields = ['comment']

class StudentAssessmentForm(forms.ModelForm):
    course_id = forms.ModelChoiceField(queryset=Course.objects.all())
    class Meta:
        model = StudentAssessment
        fields = ['course_feedback', 'teacher_feedback', 'improvements']
        widgets = {
            'course_feedback': forms.Textarea(attrs={'placeholder': 'Your feedback about the course'}),
            'teacher_feedback': forms.Textarea(attrs={'placeholder': 'Your feedback about the teacher'}),
            'improvements': forms.Textarea(attrs={'placeholder': 'What could be improved?'}),
        }