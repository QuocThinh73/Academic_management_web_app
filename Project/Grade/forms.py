from django import forms
from django.core.exceptions import ValidationError
from .models import Grade

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['assignment_score', 'midterm_score', 'final_score']

    def clean_assignment_score(self):
        score = self.cleaned_data.get('assignment_score')
        if score is not None and (score < 0 or score > 10):
            raise ValidationError('Điểm không hợp lệ.')
        return score

    def clean_midterm_score(self):
        score = self.cleaned_data.get('midterm_score')
        if score is not None and (score < 0 or score > 10):
            raise ValidationError('Điểm không hợp lệ.')
        return score

    def clean_final_score(self):
        score = self.cleaned_data.get('final_score')
        if score is not None and (score < 0 or score > 10):
            raise ValidationError('Điểm không hợp lệ.')
        return score
