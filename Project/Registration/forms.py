from django import forms
from .models import RegistrationCourse

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationCourse
        fields = ['subject', 'semester']
