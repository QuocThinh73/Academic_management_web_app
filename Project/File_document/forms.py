from django import forms
from .models import Document
from django.forms import modelformset_factory

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['description', 'course_file']
        
DocumentFormSet = modelformset_factory(
    Document,
    form=DocumentForm,
    extra=1,  # Số forms trống để hiển thị mặc định
    can_delete=True  # Cho phép xóa các tài liệu thông qua formset
)