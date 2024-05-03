from django import forms
from .models import Course

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['description', 'syllabus', 'course_file']

