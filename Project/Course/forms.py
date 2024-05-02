from django import forms
<<<<<<< HEAD
from .models import TeacherAssessment

class TeacherAssessmentForm(forms.ModelForm):
    class Meta:
        model = TeacherAssessment
        fields = ['course', 'student', 'teacher', 'grade', 'comment']
=======
from .models import Course

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['description', 'syllabus', 'course_file']
>>>>>>> 8775de51e679517688a56f13765a14a84f0c0786
